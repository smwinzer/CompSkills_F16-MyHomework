#!/usr/bin/env python3.5

#This is the program for HW5 that is written to be completely executable on its own
#To run program, ./parseHiseq.py inputfilename.fasta outputfilename.txt

#Input arguments from stdin

from sys import argv as args

program, input, output = args

#Create dictionaries for storing data

sequenceData = {}
sequences = {}

#Define function for reading in the input file
def read_input(fp):
	name = None
	seq = []
	for line in fp:
		line = line.rstrip()
		if line.startswith(">"):
			if name:
				yield (name, "".join(seq))
			name, seq = line, []
		else:
			seq.append(line)
	if name:
		yield (name, ''.join(seq))

#Extract information from input file by parsing
with open(output, '+a') as Output:
	with open(input, 'r') as Info:
		for name, seq in read_input(Info):
		
			Technology, sampleID, Primers, gene = name[1:].split()
			
			#Extract technology type
			Technology = Technology.split(':')
			Technology = Technology[0][1:]

			#Extract forward and reverse primers
			Primers = Primers.split('|')
			fwdPrimer, revPrimer = Primers[0], Primers[2]

			#Extract gene name
			gene = gene.split('|')
			gene = gene[0]
	
			#Extract country of origin
			Origin = sampleID.split(':')
			Origin = Origin[3][:2]

			#Create sampleID
			sampleID = sampleID.split(':')
			sampleID = sampleID[3]+'_'+gene
	
			#Define the nucleotides to count GC content
			A = seq.count("A")
			G = seq.count("G")
			C = seq.count("C")
			T = seq.count("T")
			GC = (G+C) / (A+G+C+T)
			
			#Add sequence information to appropriate dictionary
			sequenceData[sampleID] = {
				'Technology' : Technology,
				'Forward Primer' : fwdPrimer,
				'Reverse Primer' : revPrimer,
				'Gene' : gene,
				'Origin' : Origin,
				'GC content' : GC
				}
			Output.write( "Technology: %s\tfwdPrimer: %s\trevPrimer: %s\tgene: %s\tOrigin: %s\tGC content: %s\n" % ( Technology, fwdPrimer, revPrimer, gene, Origin, GC))
			
			#Add sequences to appropriate dictionary
			sequences[sampleID] = seq
			
# Determining the length of individual sequences
	Length = [len(v) for v in sequences.values()]

# Using a for loop to determine nucleotide content for each sequence 
	listsequences = []
	for key, value in sequences.items():
		nucs = ['A', 'C', 'T', 'G']
		count = [value.count(x) for x in nucs]
		listsequences.append((count[1]+count[3]) / (count[0]+count[1]+count[2]+count[3]))
		GC = sum(listsequences) / 1753
	
	Output.write("Input File: %r\t" % (input))
	Output.write("Output File: %r\t" % (output))
	Output.write("Number of sequences: %d\t\n" % len(sequences))
	Output.write("Average length of sequences: %r\t" % (sum(Length)/1753))
	Output.write("Average GC content: %r" % (GC))
