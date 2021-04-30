import numpy as np
import numpy.random as r
import time as t
import pandas as pd


class person:
    
    def __init__(self, status="S"):
        
        self.status = status
        self.previouslyInfected = False
        self.quarantining = False
        self.vaccinated = False
        self.travelling = False
        self.daysInfected = 0
        
    def updateProbabilities(self):
        
        if self.status == "S":
            # self.infectedNeighbours = self.neighbours.count('I')
            # self.pInfection = self.infectedNeighbours * 0.01
            self.pInfection = self.neighbours.count("I") * 0.01
            
              
        elif self.status == "I":
            if self.daysInfected >= 4 :
                if self.daysInfected <= 10:
                    self.pDeath = (self.daysInfected - 3) * 0.01
                else:
                    self.pDeath = 0.07
              
    def updateStatus(self):
        """determine new status of a person"""
        rand = r.random()
        
        # susceptible 
        # can be infected by surrounding people or infected travellers
        if self.status == "S":
            
            if rand < self.pInfection:
                self.status = "I"
            
            elif rand < self.pVaccinate:
                self.vaccinated == True
            
            elif rand < self.pQuarantine:
                self.quarantining == True
                
        # infected 
        # can recover, quarantine, die, travel or remain unchanged
        elif self.status == "I":
            
            self.daysInfected += 1
            
            if  rand <self.pDeath:
                self.status = "D"
                
            elif rand < self.pTravel:
                self.travelling == True
            
            elif rand < self.pRecovery:
                self.status == "S"
                
        # quarantined
        # can recover, die, end quarantine early or remain unchanged
        elif self.quarantining:
            
            self.daysQuarantining += 1
            
            if rand < self.pEndQuarantine:
                self.quarantining == False
            
            
    def __str__(self):
        return self.status



class subPopulationSim:
    """
    creates a 'sub-population' e.g. a city of people, 
    which can be updated each day to determine new status of each person
    """

    def __init__(self, width=5, height=5, pDeath=0.001,
                  pRecovery=0.1, pReinfection=0.005,
                 pTravel=0.01, pQuarantine=0.15, city='City',
                 pEndQuarantine=0.05
                 ):

        self.city = city
        self.width = width
        self.height = height

        self.pEndQuarantine = pEndQuarantine
        self.pDeath = pDeath
        self.pRecovery = pRecovery
        self.pReinfection = pReinfection
        self.pTravel = pTravel
        self.pQuarantine = pQuarantine
        self.pInfectedByTraveller = 0

        self.day = 0

        # initalise grid of statuses, with susceptible people
        self.gridState = [[person() for x in range(width)] for y in range(height)]


    def emptyLocation(self, pEmpty=0.01):
        """randomly make some grid points empty, with probability pEmpty"""

        for i in range(len(self.gridState)):
            for j in range(len(self.gridState[i])):
                if r.random() < pEmpty:
                    self.gridState[i][j] = None
                    # Note: numpy changes None to 'N'


    def randomInfection(self, pInitialInfection=0.5):
        """randomly infect, with probability pInitialInfection"""

        for i in range(len(self.gridState)):
            for j in range(len(self.gridState[i])):
                if r.random() < pInitialInfection and type(self.gridState[i][j]) == person:
                    self.gridState[i][j].status = "I"
                    
                    
    def updateSubPopulation(self):
        """updates whole subpopulation"""

        # initialise updated grid 
        updatedGrid = self.gridState.copy()

        for i in range(len(self.gridState)):
            for j in range(len(self.gridState[i])):
                updatedGrid[i,j] = self.updateStatus(i,j)

        # update gridState
        self.gridState = updatedGrid


    def updateStatus(self, i, j):
        
        status = self.gridState[i, j]
        rand = r.random()

    
        # recovered or vaccinated
        # may become susceptible again, or remain unchanged
        if status == 'R' or status == 'V':
            if rand < self.pReinfection:
                return 'S'
            else:
                return status

        # infected traveller 
        # may return, recover or remain unchanged
        elif status == 'T':

            if rand < self.pTravel:
                return 'I'
            elif rand < self.pRecovery:
                return 'R'
            else:
                return status

    


    def TravelCount(self):
        """ determines amount of travelled people in the grid at any one time"""
        #convert grid into a list of lists of person states
        Grid = [list(row) for row in self.gridState]

        #convert the list of lists into a list of states in the grid
        Statuses = []
        for row in Grid:
            Statuses += row

        TravelCount = Statuses.count('T')

        return TravelCount


    def identifyNeighbours(self):
        
       for i in range(len(self.gridState)):
            for j in range(len(self.gridState[i])):
                if type(self.gridState[i][j]) == person:
                    """updates probility of person being infected, if susceptible"""
            
                    # define 'local area' of an i,j grid point
                    if i == 0:
                        iMin = 0
                    else:
                        iMin = i-1
            
                    if j == 0:
                        jMin = 0
                    else:
                        jMin = j-1
            
                    iMax = i+2
                    jMax = j+2
            
                    tempGrid = np.array(self.gridState)
                    # tempGrid[i,j] = None
            
                    localGrid = [list(row) for row in tempGrid[iMin:iMax,jMin:jMax]]
                   
    
            # gather and count infection status in local area
                    self.gridState[i][j].neighbours=[]
                    for row in localGrid:
                        self.gridState[i][j].neighbours += row
                    self.gridState[i][j].neighbours = [person.status for person in self.gridState[i][j].neighbours if person != None] 
               

    def collectData(self):
        susceptable = []
        infected = []
        recovered = []
        travelled = []
        quarantined = []
        dead = []
        vaccinated = []
        for i in range(len(self.gridState)):
            for j in range(len(self.gridState[i])):
                if self.gridState[i][j].status == 'I':
                    infected += 'I'
                elif self.gridState[i][j].status == 'S':
                    susceptable += 'S'
                elif self.gridState[i][j].status == 'R':
                    recovered += 'R'
                elif self.gridState[i][j].status == 'D':
                    dead += 'D'
                elif self.gridState[i][j].status == 'T':
                    travelled += 'T'
                elif self.gridState[i][j].status == 'Q':
                    quarantined += 'Q'
                elif self.gridState[i][j].status == 'V':
                    vaccinated += 'V'

        data = pd.DataFrame(
            [len(susceptable), len(infected), len(recovered), len(dead), len(travelled), len(quarantined),
             len(vaccinated)],
            columns=["Population"], index=['Susceptible',
                                           'Infected',
                                           'Recovered',
                                           'Dead',
                                           'Travelling',
                                           'Quarantining',
                                           'Vaccinated'])
        # NOTE: rather than printing within method, do nothing, so have option to
        #       print outside of method 
        PopulationTotal = len(infected) + len(susceptable) + len(recovered) + len(dead) + len(vaccinated) + len(
            quarantined) + len(travelled)
        print(f"Total population: {PopulationTotal}")

        PercentInfected = 100 * len(infected) / PopulationTotal
        PercentSusceptable = 100 * len(susceptable) / PopulationTotal
        PercentRecovered = 100 * len(recovered) / PopulationTotal
        PercentDead = 100 * len(dead) / PopulationTotal
        PercentVaccinated = 100 * len(vaccinated) / PopulationTotal
        PercentQuarantined = 100 * len(quarantined) / PopulationTotal
        PercentTravelled = 100 * len(travelled) / PopulationTotal

        data2 = pd.Series([PercentSusceptable, PercentInfected, PercentRecovered, PercentDead, PercentTravelled,
                           PercentQuarantined, PercentVaccinated], name='Population State Percentages (%)',
                          index=['Susceptible',
                                   'Infected',
                                   'Recovered',
                                   'Dead',
                                   'Travelling',
                                   'Quarantining',
                                   'Vaccinated'])
        data['Population State Percentages (%)'] = data2

        print(f"{data}\n------------------------------------------------")

    def __str__(self):
        """for use in print function: prints current grid state"""
        tempGrid = np.array(self.gridState)
        for i in range(len(tempGrid)):
            for j in range(len(tempGrid[i])):
                tempGrid[i][j] = str(tempGrid[i][j])
        return str(tempGrid)

    "For use in grid Animation gets a colour grid to be plotted"
    def get_Colours (self):
        colour_grid =np.zeros((self.width,self.height,3),int)
        for i in range(len(self.gridState)):
          for j in range(len(self.gridState[i])):
             if  self.gridState[i][j].status == 'S':
                colour_grid[i][j][0]=0
                colour_grid[i][j][1]=255
                colour_grid[i][j][2]=0
             elif self.gridState[i, j].status == 'I':
               colour_grid[i][j][0]=255
               colour_grid[i][j][1]=0
               colour_grid[i][j][2]=0
             elif self.gridState[i, j].status == 'V':
               colour_grid[i][j][0]=0
               colour_grid[i][j][1]=0
               colour_grid[i][j][2]=255
             elif self.gridState[i, j].status == 'D':     
                colour_grid[i][j][0]=0
                colour_grid[i][j][1]=0
                colour_grid[i][j][2]=0
             elif self.gridState[i][j].status == 'Q': 
                colour_grid[i][j][0]=200
                colour_grid[i][j][1]=50
                colour_grid[i][j][2]=100
             elif self.gridState[i, j].status == 'R': 
                colour_grid[i][j][0]=50
                colour_grid[i][j][1]=50
                colour_grid[i][j][2]=250
             elif self.gridState[i, j].status == 'T': 
                colour_grid[i][j][0]=30
                colour_grid[i][j][1]=100
                colour_grid[i][j][2]=150
        
        return(colour_grid)
            

class populationSim:
    """
    simulates multiple subpopulations and people travelling between them
    """


    def __init__(self, N=5, pInfection = 0.5):
        # NOTE: Can change to input list of cities, to make more generalised,
        #       then for methods, just loop through list. 
        #       The list would be manually created outside the class
        self.Bristol = subPopulationSim(width=N, height=N, pInfection = pInfection)
        self.Cardiff = subPopulationSim(width=N, height=N, pInfection = pInfection)
        self.pInfectedByTraveller = 0
        self.pInfection = pInfection


    def populationTravel(self):
        """defines probabilty of being infected by traveller"""
        TravelledNum = self.Bristol.TravelCount() + self.Cardiff.TravelCount()
        GridPoints = self.Bristol.width*self.Bristol.height + self.Cardiff.width*self.Cardiff.height
        self.pInfectedByTraveller = (TravelledNum / GridPoints)*self.pInfection


    def updatePopulation(self):
        """assigns new traveller infection and updates each subpopulation"""
        self.populationTravel()

        self.Bristol.pInfectedByTraveller=self.pInfectedByTraveller
        self.Cardiff.pInfectedByTraveller=self.pInfectedByTraveller

        self.Bristol.updateSubPopulation()
        self.Cardiff.updateSubPopulation()


    def __str__(self):
        """for use in print function: prints all current grid states"""
        return 'Bristol:\n'+str(self.Bristol)+'\n\n'+'Cardiff:\n'+str(self.Cardiff)+'\n\n\n'






x = subPopulationSim()

x.randomInfection()
x.identifyNeighbours()
y = x.gridState[1][1]
y.updateProbabilities()
print(y, y.pInfection)
print(x)
