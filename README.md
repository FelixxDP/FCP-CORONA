# FCP-CORONAHOW TO RUN THE PROGRAMME:The programme can be run in two ways; 1) With arguments inputted by the user 2) Using pre set scenarios To run the programme using your own arguemtns type ./MAIN -h which will output the following:  --size N         Use a N x N simulation grid  --cities N       Create N cities  --duration T     Simulate for T days  --distancing P   Proportion of empty grid squares  --recovery P     Probability of recovery (per day)  --infection P    Probability of infecting a neighbour (per day)  --reinfection P  Probability of losing immunity (per day)  --death P        Probability of dying when infected (per day)  --cases P        Probabilty of initial infection  --vaccinate P    Probability of vaccination (per day)  --quarantine P   Probability of quarantine when infected (per day)  --travel P       Probability of travelling while infected (per day)  --plot           Generate plots instead of an animation  --file N         Filename to save to instead of showing on screen  --sim N          Run predetermined simulationThese are all the different arguments, if the user chooses not to use thier own argument for someof the arguments a default value will be used. e.g. if the user didn't choose a death probability then the default value 0.02087 will be used. The default values are as follows: