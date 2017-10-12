# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 13:10:32 2015

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# __________________ READ FILE ______________

Olorgesailie = pd.read_csv('Olorgesailie.csv', header = 0)

# __________________ LONG TO WIDE ______________

# check how the data looks like and the names of the columns
Olorgesailie.head()
# turn the long data into wide data
Olorgesailie = Olorgesailie.pivot(index = 'Locality', columns = 'attribute', values = 'value')
# check how the data looks like now
print Olorgesailie.head()

# ensure that numerical values are treated as numbers not as strings
Olorgesailie = Olorgesailie.convert_objects(convert_numeric=True)
# check what type of data each column contains
Olorgesailie.info()


# __________________ COLUMN ORDER ______________

# get the names of the column
print list(Olorgesailie.columns.values)
# order the columns 
cols = ['Level','Strata', 'Heavy.duty.tools', 'Large.cutting.tools', 'Large.scrapers',  'Other.large.tools','Small.tools', 'Spheroids', 'BLCT', 'CB', 'CH', 'CHA', 'CL', 'CS', 'HA', 'KN', 'LFS', 'OLT', 'OST', 'PAT', 'PHA', 'SP', 'SSNP', 'SSS'] 
# pass it back to the data
Olorgesailie = Olorgesailie[cols]
# check if everything worked fine
print Olorgesailie.head()

# __________________ MISSING VALUES ______________

# check if there are any missing data
print Olorgesailie.isnull().sum()
# check which row the missing data is
Olorgesailie[np.isnan(Olorgesailie['HA'])] # note that 'HA' can be replaced with any column name

# remove all rows with NaNs
Olorgesailie_noNaNs = Olorgesailie.dropna(axis = 0, how = 'any')
# check if it worked
print Olorgesailie_noNaNs.isnull().sum()

# replace NaNs with zeros
Olorgesailie_NaN0 = Olorgesailie.fillna(0)
# check if it worked
print Olorgesailie_NaN0.isnull().sum()

# see the difference between dropping and replacing rows with NaNs
Olorgesailie['Other.large.tools'].dropna().mean() 
Olorgesailie.fillna(0.0)['Other.large.tools'].mean()

# __________________ INCORRECT VALUES ______________

# find all unique values in the data frame
pd.unique(Olorgesailie.values.ravel())

# change the incorrect notation of presence/absence
Olorgesailie['Spheroids'] = Olorgesailie['Spheroids'].replace(-1, 0)
Olorgesailie['Spheroids'] = Olorgesailie['Spheroids'].astype(bool)

# replace incorrect values with NaNs
Olorgesailie = Olorgesailie.replace('-5', np.nan)

# check if it all worked
pd.unique(Olorgesailie.values.ravel())

# __________________ SUBSETTING THE DATASET ______________

# access a column
Olorgesailie['HA'] # note the square brackets 

# access a row 
Olorgesailie.iloc[1]  # first row of the data
Olorgesailie[:5] # first five rows

# access a specific value
Olorgesailie['HA'][3] # third row of the column 'HA'
Olorgesailie['HA'][:5] # first five rows of the column 'HA'

# subsetting data
handaxes = Olorgesailie[['Level', 'Strata', 'Large.cutting.tools', 'HA']]
print handaxes.head()

# subsetting data, omitting the first 3 rows
handaxes_selection = Olorgesailie[['Level', 'Strata', 'Large.cutting.tools','HA']] [3:]
print handaxes_selection.head()

# removing a column from the dataframe
handaxes_noLCTs = handaxes.drop(['Large.cutting.tools'], axis = 1)
print handaxes_noLCTs.head()

# subsetting data using a condition 
handaxes_lower = handaxes[handaxes['Level']=='Lower'] # select all rows where the value in column 'Level' is 'Lower'
print handaxes_lower

# subsetting data using a condition
large_assemblage = handaxes[handaxes['HA'] > 3] # select all rows where the value is larger than 3
print large_assemblage

# sampling data
handaxes_sample = handaxes.sample(n = 5)


