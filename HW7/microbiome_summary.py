#!/usr/bin/env python2.7

#This is the code for HW7 which consists of a few mathematical manipulations of data from vaginal_communities.txt

#Read data file into pandas data frame

import pandas as pd

summaryByDay = pd.read_csv('vaginal_communities.txt', sep = '\t' )

#Change OTU counts to relative abundances

summaryByDay['Lactobacillus_crispatus'] = summaryByDay['Lactobacillus_crispatus'] / summaryByDay['Total']
summaryByDay['Lactobacillus_iners'] = summaryByDay['Lactobacillus_iners'] / summaryByDay['Total']
summaryByDay['Lactobacillus_gasseri'] = summaryByDay['Lactobacillus_gasseri'] / summaryByDay['Total']
summaryByDay['Lactobacillus_jensenii'] = summaryByDay['Lactobacillus_jensenii'] / summaryByDay['Total']
summaryByDay['Atopobium_vaginae'] = summaryByDay['Atopobium_vaginae'] / summaryByDay['Total']
summaryByDay['Megasphaera_sp._type_1'] = summaryByDay['Megasphaera_sp._type_1'] / summaryByDay['Total']
summaryByDay['Streptococcus_anginosus'] = summaryByDay['Streptococcus_anginosus'] / summaryByDay['Total']
summaryByDay['Prevotella_genogroup_3'] = summaryByDay['Prevotella_genogroup_3'] / summaryByDay['Total']
summaryByDay['Clostridiales'] = summaryByDay['Clostridiales'] / summaryByDay['Total']
summaryByDay['Enterococcus_faecalis'] = summaryByDay['Enterococcus_faecalis'] / summaryByDay['Total']
summaryByDay['Corynebacterium_accolens'] = summaryByDay['Corynebacterium_accolens'] / summaryByDay['Total']

#Drop unnecessary columns

summaryByDay = summaryByDay.drop(['ID','time','sampleID','Day','Date','Batch_ID'],axis=1)

#Add a column with the Shannon Diversity Index for each row (called Shannon)

import numpy as np

def shannon(x):
	return ((np.log(x)*x).sum(axis=1))
	

summaryByDay['Shannon'] = shannon(summaryByDay[summaryByDay.columns[2:12]])

#Add a column with the Inverse Simpson Diversity Index for each row (called ISDI)

def simpson(x):
	return(1./(x**2).sum(axis=1))

summaryByDay['ISDI'] = simpson(summaryByDay[summaryByDay.columns[2:12]])

#Create summaryByWeek dataframe without prior shannon and simpson 

summaryByWeek = summaryByDay[summaryByDay.columns[:14]]

#Average all columns by patient then by week

summaryByWeek = summaryByWeek.groupby(['patientID','Week']).mean()

#Add columns for shannon diversity and inverse simpson

summaryByWeek['Shannon'] = shannon(summaryByWeek[summaryByWeek.columns[2:12]])
summaryByWeek['ISDI'] = simpson(summaryByWeek[summaryByWeek.columns[2:12]])

#Create summaryByWoman dataframe without prior shannon and simpson

summaryByWoman = summaryByDay[summaryByDay.columns[:14]]

#Average all columns by patient

summaryByWoman = summaryByWoman.groupby('patientID').mean()

#Add columns for shannon diversity and inverse simpson

summaryByWoman['Shannon'] = shannon(summaryByWoman[summaryByWoman.columns[2:12]])
summaryByWoman['ISDI'] = simpson(summaryByWoman[summaryByWoman.columns[2:12]])

#Print to txt files

summaryByDay.to_csv('summaryByDay.txt', sep = '\t')

summaryByWeek.to_csv('summaryByWeek.txt', sep = '\t')

summaryByWoman.to_csv('summaryByWoman.txt', sep = '\t')
