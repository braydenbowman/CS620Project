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

# Define main function
def main():
    data = pd.read_csv(sys.argv[1], index_col=0)
    data1 = data[]
    data1 = data1.assign(WR=lambda x : x.WHG - x.WAG)
    print(data1)

# Execute main() function
if __name__ == '__main__':
    main()