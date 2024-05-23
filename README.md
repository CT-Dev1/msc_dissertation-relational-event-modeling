# thesis

This repository is for my postgraduate thesis "A Longitudinal Network Analysis of Online Collective Action: Reddit’s r/amcstock Community"

It seeks to investigate the collective action dynamics of r/amcstock in relation to the successful shortsqueeze achieved in June 2021.

This is currently a early-stage version of the code. It will be updated as my methods are finalized in the coming months. I will update periodically. 

All data is derived from the push shift data dump at academic torrents, includes all 2021 comments and submissions, here is the [link](https://academictorrents.com/details/9c263fc85366c1ef8f5bb9da0203f4c8c8db75f4)

# Code Directory

### scripts/raw_parsing
- zst_to_csv.py - module for zst to csv conversion function - decompresses the zst compressed push shift file - courtesy of [u/ramnamsatyahai](https://www.reddit.com/r/pushshift/comments/1cptl87/trouble_with_zst_to_csv/) 
- combine_folder_multiprocess.py - script to filter raw zst files from pushshift dump - courtesy of [Watchful1](https://github.com/Watchful1/PushshiftDumps)

### scripts/network_parsing
