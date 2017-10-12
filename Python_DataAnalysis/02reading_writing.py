# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:41:21 2015

@author: user
"""
# import libraries
import pandas as pd
import matplotlib.pyplot as plt         
                     
#__________ READ A FILE __________
Acheul_Afr = pd.read_csv("Acheulean.csv", header = 0) # read in the file
print Acheul_Afr.head()                  # check how the data looks like

#__________ PLOT THE DATA __________
plt.style.use('ggplot')                 # this line makes the graphs prettier
Acheul_Afr.hist(figsize = (10,10))      # summary plot of the data

#__________ WRITE TO FILE __________
Location_output = 'Acheul_Afr.csv'      # specify where to save the file to
Acheul_Afr.to_csv(Location_output)      # save the .csv