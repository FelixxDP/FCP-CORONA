# FCP-CORONA

HOW TO RUN THE PROGRAMME:
The programme can be run in two ways; 
1) With arguments inputted by the user 
2) Using pre set scenarios 

To run the programme using your own arguemtns type ./MAIN -h which will output the following:
-  --size N         Use a N x N simulation grid
-  --cities N       Create N cities
-  --duration T     Simulate for T days
-  --distancing P   Proportion of empty grid squares
-  --recovery P     Probability of recovery (per day)
-  --infection P    Probability of infecting a neighbour (per day)
-  --reinfection P  Probability of losing immunity (per day)
-  --death P        Probability of dying when infected (per day)
-  --cases N        Number of initial infections
-  --vaccinate P    Probability of vaccination (per day)
-  --quarantine P   Probability of quarantine when infected (per day)
-  --travel P       Probability of travelling while infected (per day)
-  --plot           Generate plots instead of an animation
-  --file N         Filename to save to instead of showing on screen
-  --sim N          Run predetermined simulation

These are all the different arguments, when entering a probability ensure the value is between 0 and 1. 
If the user chooses not to use thier own argument for some of the arguments a default value will be used. 
e.g. if the user didn't choose a death probability then the default value 0.002087 will be used. The default values chosen from real world data 
(see report for referencing) are as follows.
- size = 50 x 50
- cities = 2
- duration = 100 days
- distancing = 0.05
- recovery = 0.1
- infection = 0.3
- reinfection = 0.005
- death = 0.002087
- cases = 5
- vaccinate = 0.0001 
- quarentine = 0.15
- travel = 0.1

For example, if you wanted to run a simulation with 5 cities, 100x100 grid, 60% chance of infection and a 5%
death rate. You would write:

$ ./MAIN.py --cities=5 --size=100 --infection=0.5 --death=0.05


HOW TO RUN PREDETERMINED SIMULATIONS:
There are 12 predetermined simulations that can be run by typing:

$ ./MAIN.py --sim=N  # Where N is listed beside each scenario below

The 11 Scenarios are as follows (if an argument is not specified it has taken its default value):
1) Multiple different sized cities
- 6 cities with pTravel = 0.01 and pRandomInfection = 0.002
2) Multiple cities with Large amounts of travel
- Same 6 cities as previous however pTravel = 0.3
3) Effect of Social Distancing
- 5 50x50 cities with the following distancing 0.15, 0.3, 0.45, 0.6, 0.75 with pTravel = 0.01
4) High Quarentine vs Low Quarentine Rates
- City 1 pQuarentine = 1 and pEndQuaretine = 0 i.e. immediately entering quarentine when infected and not leaving till uninfected
- City 2 pQuarentine = 0.4 and pEndQuarentine 0.05
- City 3 pQuarentine = 0
- All have no infected travel
5) High Vaccine rate vs Low Vaccine rate (75x75 cities)
- City 1 pVaccine = 0.1
- City 2 pVaccine = 0.033
- City 3 pVaccine = 0
6) 3 Cities with different control measures (75x75 cities))
- City 1 pVaccine = 0.033, pQuarantine = 0.95, pTravel = 0, pDistancing = 0.3, pRecovery = 0.2 i.e. some vaccinations, almost everyone infected 
goes into quaretnine, no travelling and large amount of distancing
- City 2 pVaccination = 0.01, pQuarentine = 0.3, pTravel = 0.1, pRecovery = 0.1, pDistancing = 0.1 i.e. less vaccines, less distancing and less quarentining 
and a longer recovery time with more travel
- City 3 pVaccination = 0, pQuarantine = 0, pDistancing = 0, pTravel = 0.3, pRecovery = 0.075 i.e. no Measures in place, longer recovery time and
more travelling
7) Effect of Different Death Rates
- 3 cities with no travel 75x75
- pDeath = 0.002, 0.1, 0.9
8) Vaccine against no vaccines
- Cite 1 pVaccination = 0.1 which is introduced after 8 days
- City 2 pVaccination = 0 (this leads to multiple waves)
101) Mild Recovery rate case
- One city with pRecovery = 0.6 and pReinfection = 0.05 this shows the effect of immunity loss which creates several spikes 
102) Rapid Recovery case
- One city with  pRecovery = 0.99 and pReinfection = 0.05 
103) Oscilating SIR pattern case
- One city, pRecovery = 0.7, Preinfection = 0.025 and pTravel = 0
104) Poorer Areas Simulation (simulates a Deadly virus in poorer Areas)
- One city with pRecovery = 0, pDeath = 0.1 and pTravel = 0
105) Rapid Spread and Death
- One city 200x200, pDeath=0.9, pTravel = 0.2 and pInfection = 0.99
106) Rapid spread and rapid reinfection
- One city pInfection = 0.99, pRecovery = 0.99, pTravel = 0 and pReinfection = 0.99

So for example if One was to run simulation 106 they would write:
$ ./MAIN.py --sim=106

























































