#!/usr/bin/env python

#This is the code for HW9 which generates figures from the results of previous assignments.

import matplotlib.pyplot as plt
from numpy.random import randn
import pandas as pd
from pandas import DataFrame, Series
from pylab import figure, axes, pie, title, show

#Make horizontal stacked barcharts of each woman's microbiome using summaryByWoman.txt

data = pd.read_csv('summaryByWoman.txt', sep = '\t', comment='#')
data = data.sort(columns='patientID',ascending=False)
data = data.drop(['Total','Shannon','Simpson'], axis=1)
fig = data.plot(kind = 'barh',stacked=True)
plt.legend(loc='center right',prop={'size':10})
plt.xlim([0,2])
fig.set_yticklabels(data[data.columns[0]])
fig.set_xticks([0.1,0.3,0.5,0.7,0.9])
fig.set_xlabel('Relative Abundance', fontsize = 'large')
fig.set_ylabel('Patient Identifier', fontsize = 'large')
fig.set_title('Microbiome composition by woman', fontsize = 'x-large')

#Save figure as MicrobiomeByWoman.png

fig.figure.savefig('MicrobiomeByWoman.png')


