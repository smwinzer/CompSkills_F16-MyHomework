#!/usr/bin/env python

#This is the code for the final HW of the Fall semester 2016! Therefor this must be the best HW!
#This code generates a couple of figures using provided data sets, similar to HW9

#Plot the relative abundances of L. crispatus, L. iners, and L. gasseri against Shannon diversity
#First plot will be for days with Nugent scores indicating positive BV (range 7-10)
#Second plot will be for Nugent scores indicating negative BV (0-3)
#The data set to be used is summaryByDay_merged.txt

import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

#Read data set into python

data = pd.read_csv('summaryByDay_merged.txt', sep = '\t', comment='#')

#Set up figure with subplot regions

fig = plt.figure()
plot1 = fig.add_subplot(211)
plot2 = fig.add_subplot(212)

#Separate data by negative or positive nugent score

NegData = data.loc[data['Score'] < 4]
PosData = data.loc[data['Score'] > 6]

#Create the first plot for the Positive Nugent scores

plot1.scatter(PosData['Lactobacillus_crispatus'], PosData['Shannon'], marker='o', color='red', alpha=0.4, label='L. crispatus')
plot1.scatter(PosData['Lactobacillus_iners'], PosData['Shannon'], color='blue', alpha=0.4, label='L. iners')
plot1.scatter(PosData['Lactobacillus_gasseri'], PosData['Shannon'], color='green', alpha=0.4, label='L. gasseri')
plot1.legend(loc='upper right',prop={'size':10})
plot1.set_xlim([0,1])
plot1.set_ylabel('Shannon Diversity', fontsize='medium')
plot1.set_title('BV Positive Nugent Scores', fontsize='large')

#Create the second plot for the Negative Nugent scores

plot2.scatter(NegData['Lactobacillus_crispatus'], NegData['Shannon'], marker='o', color='red', alpha=0.4, label='L. crispatus')
plot2.scatter(NegData['Lactobacillus_iners'], NegData['Shannon'], color='blue', alpha=0.4, label='L. iners')
plot2.scatter(NegData['Lactobacillus_gasseri'], NegData['Shannon'], color='green', alpha=0.4, label='L. gasseri')
plot2.legend(loc='upper right',prop={'size':10})
plot2.set_xlim([0,1.])
plot2.set_xlabel('Relative Abundance', fontsize='medium')
plot2.set_ylabel('Shannon Diversity', fontsize='medium')
plot2.set_title('BV Negative Nugent Scores', fontsize='large')

#Print plot to file

fig.savefig('LG_diversity.png')

