# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:41:21 2015

@author: user
"""
from __future__ import division             # prevents integer truncation
import pandas as pd
import matplotlib.pyplot as plt          
import numpy as np  
                     
pd.options.display.mpl_style = 'default'    # makes graphs pretty

#plt.style.use('ggplot')                     # graphs in ggplot style

# ___ READING AND CHECKING DATA _____
# read in the file
snodgrass = pd.read_csv("Snodgrass.csv", header = 0) 
# check how the data looks like
print snodgrass.head() 
print snodgrass.info()
# summary plot
snodgrass.hist()
snodgrass.hist(figsize = (10, 10)) # make it a bit larger

# ______DIFFERENT TYPES OF PLOTS____
print list(snodgrass.columns.values)

#___ simple barplot
snodgrass.Points.plot(kind = 'bar', figsize = (20, 10)) # a pretty pointless bar graph

# ___ grouped barplot
# get the names of the columns containing artefact counts
snodgrass_artefacts = ['Points','Abraders','Discs', 'Earplugs', 'Effigies', 'Ceramics']  
# sort the table by area and get the mean number of each artefact type
snodgrass_areas = snodgrass.pivot_table(snodgrass_artefacts, columns = 'Segment', aggfunc = 'mean') 
# create a much more meaningful barplot
snodgrass_areas.plot(kind = 'bar') 

# ___ stacked barplot
snodgrass_areas.plot(kind = 'bar', stacked = True)  # simple stacked barplot
# split the plot into three horizontally oriented graphs, remove the legend, set the size to 10x8 inches
snodgrass_areas.plot(kind = 'barh', subplots = True,  legend = False, figsize = (10,8)) 
#  create a stacked plot, use a different colour scheme, set transparency at 0.7, give it a title
snodgrass_areas.plot(kind = 'bar', subplots = True, stacked = True, legend = False, colormap = 'Set1', alpha = 0.7, title = 'Frequencies of artefacts per area') 

# ___ boxplot
snodgrass_areas.boxplot()

# ___ scatter plot
# create a scatter plot of the pithouses, pass the 'East' and 'West' as coordinates
snodgrass_distribution = snodgrass.plot(kind = 'scatter', x = 'East', y = 'South')
# show the distribution of points by using a symbol proportional to their count
snodgrass_frequency = snodgrass.plot(kind = 'scatter', figsize = (10, 10), x = 'East', y = 'South', s=snodgrass['Points']*100, alpha = 0.6, label= 'Points')
# add a different artefact type
snodgrass.plot(kind = 'scatter', x = 'East', y = 'South', s=snodgrass['Abraders']*100,  color = 'b',alpha = 0.6, label= 'Abraders', ax = snodgrass_frequency)
# amend the legend
snodgrass_frequency.legend (title = 'Artefact types', markerscale = 0.3, loc='upper right', bbox_to_anchor=(0.99, 0.99))

# ___SAVING THE FIGURE TO A FILE
fig = snodgrass_frequency.get_figure()
fig.savefig("Snodgrass_artefact_distribution1.png", dpi = 300 )