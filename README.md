# Google Play App Figures

## Description

This project for INST 326 uses the "Google Play Store Apps" dataset from Kaggle. 
The program sorts through the data to find a few interesting items. First, the program
finds the apps with 1 billion or more downloads. Next, the program finds the
top app categories by total installs and displays this on a graph. Additionally, the program
finds the top app categories by total review count and displays this on a graph.

This program is interesting because

## Install

For my project, you will need to install and import a few items.

1: You'll need Python3 installed to run this project.

2: You'll need to import Pandas to run this project. This can be done by running this code:

    import pandas as pd

3: You'll need to import Matplotlib to run this project. This can be done by running this code:

    import matplotlib.pyplot as plt

## Run

A sample program `maryland-bills.py` will use the propublica module to go
through all the House members from Maryland and print out the bills that they
have introduced.  You can run it like this:

    python maryland-bills.py

## Test

You can run some unit tests for the propublica module using [pytest]:

    pytest test.py