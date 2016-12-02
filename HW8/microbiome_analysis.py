#!/usr/bin/env python3.5

#This is the code for HW8. It imports data from two files into pandas dataframes and indexes
#them by several variables. It then merges the two data sets into a single dataframe and
#calculates several correlations between the data sets.

import pandas as pd
import numpy as np

#Read summaryByDay.txt file from HW7 into a pandas data frame
summaryByDay = pd.read_csv('summaryByDay.txt', sep = '\t')

#Index summaryByDay by woman, week, and day
sBDi = summaryByDay.set_index(['patientID', 'Week', 'Day'])

#Read vaginal_metadata.txt into a pandas data frame
metadata = pd.read_csv('vaginal_metadata.txt', sep = '\t')

#Drop unnecessary columns from metadata
metadata = metadata.drop(['ID','DAYOFWK','RDATE'],axis=1)
#Rename columns to have same name as summaryByDay
metadata.columns = ['Day','Week','patientID', 'Score', 'VAG_INT', 'COND_USE', 'SPER_USE', 'PARTNER', 'MENSTRUA', 'TAMPON', 'MEDS', 'MEDS_SP']

#Index metadata by woman, week, and day
mdi = metadata.set_index(['patientID','Week','Day'])

#Merge the two dataframes by index
combined = pd.merge(summaryByDay, metadata, left_index=True, right_index=True)

#Compute correlations of the shannon and simpson diversity indexes
combined['Shannon'].corr(combined['Simpson']) #Correlation is 0.95297

#Compute the correlations for Score through Meds with the Shannon diversity index
subset = combined[combined.columns[20:28]]
output = subset.corrwith(combined['Shannon'])

#Print correlations to file
output.to_csv('Correlations.txt', sep = '\t')

#Compute correlations of OTU relative abundances with Score and Meds
subset2 = combined[combined.columns[3:14]]
output2 = subset2.corrwith(combined['Score'])
output3 = subset2.corrwith(combined['MEDS'])

output2.to_csv('Correlations.txt', header=None, mode='a', sep='\t')
output3.to_csv('Correlations.txt', header=None, mode='a', sep='\t')

