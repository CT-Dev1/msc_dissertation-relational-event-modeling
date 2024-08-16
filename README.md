# Msc Dissertation

This repository is for my postgraduate dissertation "A Relational Event Model Approach to Online Collective Action: Reddit’s r/amcstock"

Abstract:
This paper investigates the Reddit-driven AMC short squeeze of 2021 as a casestudy of online collective action. It leverages unique features of the movement to conduct a novel analysis of longitudinal interaction patterns among Reddit users, relating these to the movement’s growth, climax, and decline over a 17-month period. Relational event models are adapted to accommodate large-scale dynamic interaction data using case-control sampling and partial likelihood estimation, developing an approach that can be broadly applied to Internet networks. A sliding window process is used to estimate the temporal variations in the model coefficients. The study finds evidence supporting the staying power of activity and popularity effects throughout the short squeeze life-cycle. It also finds that interaction predictors fluctuate substantially in short-term trends, suggesting that the underlying social formations in the network are highly temporary. The study utilizes an ‘organizational agent’ framework of networked collective action and explores a range of possibilities in an underdeveloped area of study. It examines interaction predictors related to clustering, activity, popularity, and other dyadic effects, advancing empirical knowledge on cases of collective action, and providing a methodological foundation for further studies in this area, particularly in analyzing dynamic network behavior.

All data is derived from the push shift data dump at academic torrents, includes all 2021 comments and submissions, here is the [link](https://academictorrents.com/details/9c263fc85366c1ef8f5bb9da0203f4c8c8db75f4).

The _eventnet_ software used to run relational event model statistics is courtesy of Jeurgen Lerner, and can be downloaded from its [Github]([https://academictorrents.com/details/9c263fc85366c1ef8f5bb9da0203f4c8c8db75f4](https://github.com/juergenlerner/eventnet)). 

All models and visualizations are run in R and raw data parsing is run in Python.

# Code Directory

### eventnet_configs
These are the XML configuration files for the _eventnet_ java program specifying to the baseline, event-type and weighted model statistic calculations.

### modeling
These files specify the Cox Proportional Hazard models for the coefficient estimation process of the relational event models. They are organized into three stages corresponding to the baseline, time-varying and event type and weighted. They additionally details visualization and tables of the model outputs. Note that stage 2 details the sliding window code for longitudinal analysis of the observation period. 

### network construction 
Details the data filtering and raw data collection steps. Note that raw Reddit data comes in the form of zst compressed files, so the following folder provides script to handle this data and extract comments and submission related to a specific subreddit. 

#### raw_parsing_scripts
- zst_to_csv.py - module for zst to csv conversion function - decompresses the zst compressed push shift file - courtesy of [u/ramnamsatyahai](https://www.reddit.com/r/pushshift/comments/1cptl87/trouble_with_zst_to_csv/) 
- combine_folder_multiprocess.py - script to filter raw zst files from pushshift dump to get subreddit specific data without full decompression - courtesy of [Watchful1](https://github.com/Watchful1/PushshiftDumps)

### visualization 
Code for the visualization included in the dissertation, for missing data, case study time line visualization and structural network trends.

