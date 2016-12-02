#!/usr/bin/env python3.5

#This is the code for HW9 which generates figures from the results of previous assignments.

import matplotlib.pyplot as plt
from numpy.random import randn
import pandas as pd
from pandas import DataFrame, Series
from pylab import figure, axes, pie, title, show

#Make horizontal stacked barcharts of each woman's microbiome using summaryByWoman.txt

data = pd.read_csv('summaryByWoman.txt', sep = '\t', comment='#')
data = data.drop(['Total','Shannon','Simpson'], axis=1)
fig = data.plot(kind = 'barh',stacked=True)
fig.set_yticklabels(data[data.columns[0]])


#Save figure as MicrobiomeByWoman.png

fig.figure.savefig('test.png')

#Something you were playing with that kinda failed

fig, axes = plt.subplots(2,2)
ax = axes[0,0]

fig = deciles.plot( ax=ax, kind='bar',color='blue')
ax = axes[0,1]
fig = deciles.plot( ax=ax, kind='barh',color='yellow')

fig.set_tight_layout(True)
fig.savefig('test.png')

fig.figure.savefig('test.png') # THIS WORKS!!!!

summaryByDay = summaryByDay.drop(['ID','time','sampleID','Day','Date','Batch_ID'],axis=1)






fig.show()