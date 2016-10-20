#!/usr/bin/env python3.5

#This is the code for HW6. The purpose of this code is to... This code is written to be fully
#executable from the command line.

''' Todos:
1. Choose appropriate data structure for data file. Make sure to notate why you chose that 
particular data structure. Consider using a dictionary? Using the sampleID as a key? Will
want to be able to group the data by sampleID and timepoint.
		-How about saving in a dictionary with sampleID as a key. Wouldn't that save each entry
		as a list and make it retrievable by sampleID?
		-Also consider using key tuples between patient ID and timepoint. This may make the later
		parts of this homework simpler.
2. Change all OTU counts to relative abundances (read count / total count) If there are bad
data points, remove them. This is real data and will therefor likely have some issues.

3. Compute average relative abundance of each OTU for each patient across all time points. 

4. avgRelativeAbundances.txt is going to receive patient id and relative abundances for each OTU.
'''

