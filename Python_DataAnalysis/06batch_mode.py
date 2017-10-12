# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:46:45 2015

@author: user
"""
from __future__ import division     # prevents integer truncation
import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.mpl_style = 'default'    # makes graphs pretty


# _____________ INTRODUCING THE FOR-LOOP _____________
# read the file 
snodgrass = pd.read_csv("Snodgrass.csv", header = 0) 
snodgrass_artefacts = [ 'Points', 'Abraders', 'Discs', 'Earplugs', 'Effigies', 'Ceramics'] 
# color palette picked up from colorbrewer2.com
my_colors = ['#d73027', '#fdae61', '#ffffbf','#a6d96a', '#abd9e9',  '#4575b4']
# set up the plot
scatter1 = snodgrass.plot(kind = 'scatter', x = 'East', y = 'South', figsize = (10,10))

# the LOOP: for each element (i) in the list (snodgrass_artefacts) 
for artefact in snodgrass_artefacts:
    # determine the new colour by taking the index of i and pass it as the index of the 'my_color' list
    my_color = my_colors[snodgrass_artefacts.index(artefact)]
    # produce a plot - use i as a label
    snodgrass.plot(kind = 'scatter', x = 'East', y = 'South', s=snodgrass[artefact]*100,  color = my_color, alpha = 0.6, label= artefact, ax = scatter1)

# amend the legend, note it doesn't go into the for-loop (it's not indented) 
# that's because we don't need to amend it every time a new artefact type is plotted, we can do it once at the end
scatter1.legend (title = 'Artefact types', markerscale = 0.3, loc='upper right', bbox_to_anchor=(0.99, 0.99))
    
# _____________ CONCATENATING FILES _____________
#     
# create a list of the pithouses numbers
pithouses = range (1, 92)
# create a list of column names
columns = [ 'East', 'South', 'Length', 'Width', 'Segment', 'Inside', 'Area', 'Points', 'Abraders', 'Discs', 'Earplugs', 'Effigies', 'Ceramics', 'Total', 'Types']
# a placeholder
temp = []
# The Loop: for each element ('house') in the list ('pithouses')
for house in pithouses:
    # get the file, where %d will be the pithouse number
    path = 'snodgrass/pithouse%d.csv' %house
    # read the file and append the column names
    df = pd.read_csv(path, names = columns)
    # add the pithouse number to the 'Pithouse' column
    df['Pithouse'] = house
    # and append it to the temporary placeholder
    temp.append(df)

# concatenate all the data we put into the temporary placeholder ('temp')
# ignore the index the data got from reading in the csv files
data = pd.concat(temp, ignore_index = True)

    
    
    
    

    