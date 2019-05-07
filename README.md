# Google Play App Statistics

## Description

This project for INST 326 uses the "Google Play Store Apps" dataset from Kaggle. 
The program sorts through the data to find a few interesting items. First, the program
finds the apps with 1 billion or more downloads. Next, the program finds the
top app categories by total installs and displays this on a graph. Additionally, the program
finds the top app categories by total review count and displays this on a graph.

This program is interesting because it provides an good understanding of the mobile application marketplace. It shows which apps and categories are most popular based on install count. Additionally, using review counts per app category, it shows which categories of apps people trully care about improving.

For exmaple, Social apps have approximately 50% as many downloads as Communication apps, but almost 80% as many reviews. This could mean that users care more about improving Social apps. Or perhaps, it shows that people engage more with Social apps than Communication apps. Whatever the reason, it is surely interesting.

## Download CSV File

This program analyzes data from a CSV file found on Kaggle (https://www.kaggle.com/lava18/google-play-store-apps). The original file, called "Google Play Store Apps," required some cleanup, which I conducted in both excel and with Python. In excel I deleted duplicate rows and organized the rows alphabetically. Using Python, I removed problematic symbols and turned the "Installs" column into numeric values. The updated, clean file can be found in this project's repository under the file name "googleplaystore_326project.csv." 

## Install

For my project, you will need to install and import a few items.

1: You'll need Python3 installed to run this project.

2: You'll need to import Pandas to run this project. This can be done by running this code:

    import pandas as pd

3: You'll need to import Matplotlib to run this project. This can be done by running this code:

    import matplotlib.pyplot as plt

## Run

You can run the program by simply chosing to run the program in a terminal window, as is usually done.