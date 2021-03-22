#! usr/bin/env python
'''
Script to get regress petal length agains sepal length for each species in a dataframe
------------------------
input = csv with "species", "petal_length_cm", and "sepal_length_cm" columns
'''

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def getDataframeList(dataframe):
    '''
    subset dataframe for each species
    '''
    species_list = dataframe.species.unique()
    dataframe_list = []
    for i in species_list:
        dataframe_list.append(dataframe[dataframe.species==i])        
    return dataframe_list

def getRegPlot(x, y, xlabel_in, ylabel_in, species):
    '''
    create single scatterplot with line of best fit for each dataframe
    '''
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = species)
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel(xlabel_in)
    plt.ylabel(ylabel_in)
    plt.legend()
    plt.savefig('Plot.png')

if __name__ == '__main__':
    dataframe = pd.read_csv(sys.argv[1])
    dataframe_list = getDataframeList(dataframe)
    
    for i in dataframe_list:
        x = i.petal_length_cm
        y = i.sepal_length_cm
        species = dataframe.species.unique()[0]
        getRegPlot(x, y, "Petal length (cm)", "Sepal length (cm)" , species)
