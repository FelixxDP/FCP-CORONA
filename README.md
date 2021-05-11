# FCP-CORONAHOW TO RUN THE PROGRAMME:The programme can be run in two ways; 1) With arguments inputted by the user 2) Using pre set scenarios To run the programme using your own arguemtns type ./MAIN -h which will output the following:-  --size N         Use a N x N simulation grid-  --cities N       Create N cities-  --duration T     Simulate for T days-  --distancing P   Proportion of empty grid squares-  --recovery P     Probability of recovery (per day)-  --infection P    Probability of infecting a neighbour (per day)-  --reinfection P  Probability of losing immunity (per day)-  --death P        Probability of dying when infected (per day)-  --cases N        Number of initial infections-  --vaccinate P    Probability of vaccination (per day)-  --quarantine P   Probability of quarantine when infected (per day)-  --travel P       Probability of travelling while infected (per day)-  --plot           Generate plots instead of an animation-  --file N         Filename to save to instead of showing on screen-  --sim N          Run predetermined simulationThese are all the different arguments, when entering a probability ensure the value is between 0 and 1. If the user chooses not to use thier own argument for some of the arguments a default value will be used. e.g. if the user didn't choose a death probability then the default value 0.002087 will be used. The default values chosen from real world data (see report for referencing)are as follows.- size = 50 x 50- cities = 2- duration = 100 days- distancing = 0.05- recovery = 0.1- infection = 0.3- reinfection = 0.005- death = 0.002087- cases = 5- vaccinate = 0.0001 - quarentine = 0.15- travel = 0.1For example, if you wanted to run a simulation with 5 cities, 100x100 grid, 60% chance of infection and a 5%death rate. You would write:./MAIN.py --cities=5 --size=100 --infection=0.5 --death=0.05