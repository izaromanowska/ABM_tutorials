# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:53:20 2015

@author: user
"""
from __future__ import division
import pandas as pd
from scipy import stats 
pd.options.display.mpl_style = 'default'
# read the csv
handaxes = pd.read_csv('Handaxes.csv', header = 0)

# check the data
print handaxes.head()
handaxes.hist(figsize = (10,10))

# descriptive statistics on the full dataset
print handaxes.describe()

# L - Length, B - Breadth, T - Thickness
LBT = ['L', 'B', 'T']

# subset the data by the level to make the manipulations easier
lower_levels = handaxes[handaxes['Level'] == 'Lower'][LBT]  
middle_levels = handaxes[handaxes['Level'] == 'Middle'][LBT]  
upper_levels = handaxes[handaxes['Level'] == 'Upper'][LBT]

# plot each level 
lower_levels.hist()
middle_levels.hist() 
upper_levels.hist()

# check if the data is normally distributed
stats.normaltest(lower_levels)
stats.normaltest(middle_levels)
stats.normaltest(upper_levels)

# T-student (output = t-statistic and p-value)
print stats.ttest_ind(lower_levels['B'], upper_levels['B'])
# T-student on all variables
print stats.ttest_ind(lower_levels, upper_levels)

# WTT Rank Sum test  (output = z-statistic and p-value)
print stats.ranksums(lower_levels['L'], middle_levels['L'])

# ANOVA (output = F-value and p-value)
print stats.f_oneway(lower_levels, middle_levels, upper_levels)