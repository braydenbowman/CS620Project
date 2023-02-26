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

# Define 
def analyzeWinLose(data):
    data1 = data
    data1 = data1.assign(WR=lambda x : x.WHG - x.WAG)
    plt.hist(data1['WR'])
    return

# Define 
def analyzeEfficiency(data):
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
