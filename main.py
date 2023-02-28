'''
CS 620 Project
Authors: Christopher Sanders, Brayden Bowman, Ismail Rabiu
'''

# Python Imports
import sys

# Outside Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global Variables
figure = -1

# Get unique figure number
def getFigureNumber():
    global figure
    figure += 1
    return figure

# Define Win Lose Analysis
def analyzeWinLose(data):
    # Analyze win differential  
    data = data.assign(WD=lambda x : x.WHG - x.WAG)
    plt.figure(getFigureNumber())
    plt.hist(data['WD'])

    # Analyze loss differential
    data = data.assign(LD=lambda x : x.LHG - x.LAG)
    plt.figure(getFigureNumber())
    plt.hist(data['LD'])

    # Analyze win rate 
    data = data.assign(WR=lambda x : x.WHG / x.LHG)
    plt.figure(getFigureNumber())
    plt.hist(data['WR'])

    # Analyze win rate 
    data = data.assign(LR=lambda x : x.WAG / x.LAG)
    plt.figure(getFigureNumber())
    plt.hist(data['LR'])

    return

# Define 
def analyzeEfficiency(data):
    # Analyze Defense ratio 
    data = data.assign(HAR=lambda x : x.DEHG / x.DEAG)
    plt.figure(getFigureNumber())
    plt.hist(data['HAR'])

    return

# Define 
def analyzeFreeThrows(data):

    return

# Define 
def analyzeTurnovers(data):
    
    return

# Define main function
def main():
    # Load Data
    data = pd.read_csv(sys.argv[1], index_col=0)

    # Run analysis of the data
    analyzeWinLose(data)
    analyzeEfficiency(data)
    analyzeFreeThrows(data)
    analyzeTurnovers(data)

    # Show Plots
    plt.show()

# Execute main() function
if __name__ == '__main__':
    main()
