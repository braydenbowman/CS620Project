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
    data = data.assign(LD=lambda x : x.LHG - x.LAG)

    plt.figure(getFigureNumber())
    plt.boxplot([data['WD'], data['LD']], labels=['Win Difference', 'Loss Difference'])
    plt.title("Difference of Home Wins and Away Wins for All Teams")
    plt.xlabel("Difference of Wins and Losses Home and Away")
    plt.ylabel("Difference")
    plt.show(block=False)

    total_home_wr_avg = data['WHG'].mean()
    total_home_lr_avg = data['LHG'].mean()
    plt.figure(getFigureNumber())
    plt.title("Home Win Rate and Away Loss Rate")
    plt.ylabel("Win Rate %")
    plt.bar(["Home Win Rate", "Away Loss Rate"] ,[100 * (total_home_wr_avg/41), 100 * (total_home_lr_avg/41)], width=0.5)
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show(block=False)

    return

# Define 
def analyzeEfficiency(data):
    # Analyze Defense and Offense ratio 
    plt.figure(getFigureNumber())
    plt.boxplot([data['DEHG'], data['DEAG'], data['OEHG'], data['OEAG']], labels=['Home Defensive Efficiency', 'Away Defensive Efficiency', "Home Offensive Efficiency", "Away Offensive Efficiency"])
    plt.xticks(rotation=45)
    # Set the title and axis labels
    plt.title("Box Plot of Defensive and Offensive Efficiency Home and Away")
    plt.xlabel("Home/Away and Offensive/Defensive")
    plt.ylabel("Efficiency Coefficient")
    plt.tight_layout()

    plt.show(block=False)

    return

# Define 
def analyzeFreeThrows(data):
    # Analyze Free throw Home and Away 
    # Get the columns
    ftp_cols = ['FTPHG', 'FTPAG']
    data = data[ftp_cols]

    # Create a horizontal bar chart of the FTPHG and FTPAG columns
    ax = data.plot(kind='barh', width=0.8, figsize=(10,8))

    # Labels
    ax.set_xlabel('Free Throw Percentages')
    ax.set_ylabel('Team')
    ax.set_title('Comparison of Home Game Free Throw % and Away Game Free Throw % by Team')
    ax.legend(['FTPHG', 'FTPAG'], loc='upper right')

    #Plot
    plt.figure(getFigureNumber())
    plt.show(block=False)

    plt.boxplot([data['FTPHG'], data['FTPAG']], labels=['Home', 'Away'])

    # Set the title and axis labels
    plt.title("Box Plot of Free Throw Percentages Home and Away")
    plt.xlabel("Home/Away")
    plt.ylabel("Free Throw Percentage")

    plt.show(block = False)

    return

# Define 
def analyzeTurnovers(data):
    # Analyze Free throw Home and Away 
    # Get the columns
    ftp_cols = ['THG', 'TAG']
    data = data[ftp_cols]

    # Create a horizontal bar chart of the FTPHG and FTPAG columns
    ax = data.plot(kind='barh', width=0.8, figsize=(10,8))

    # Labels
    ax.set_xlabel('Turnovers Per Game')
    ax.set_ylabel('Team')
    ax.set_title('Comparison of Home Game Turnovers and Away Game Turnovers by Team')
    ax.legend(['THG', 'TAG'], loc='upper right')

    #Plot
    plt.figure(getFigureNumber())
    plt.show(block=False)
    
    plt.clf()
    plt.boxplot([data['THG'], data['TAG']], labels=['Home', 'Away'])

    # Set the title and axis labels
    plt.title("Box Plot of Turnovers Per Game Home and Away")
    plt.xlabel("Home/Away")
    plt.ylabel("Turnovers Per Game")

    plt.show(block = False)
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
