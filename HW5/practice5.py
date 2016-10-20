#!/usr/bin/env python3
# Make this a runnable program

from sys import argv as args

script, fasta, output = args

#get arguments from stdin

sequenceData = {}
sequences = {}

def read_fasta(fp):
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

with open(output, '+a') as seqDataOutput:
	with open(fasta, 'r') as Info:
		for name, seq in read_fasta(Info):
		
			runInfo, sampleInfo, primerInfo, geneInfo = name[1:].split()
			
			# Split sample ID to contain country and gene information
			sampleID = sampleInfo.split (':')[-2]+ '_' + sampleInfo.split(':')[-1]
		
			# Calls technology information
			technology = runInfo.split (':')[0]
				
			# Calls country of origin out of the gene information
			country = sampleInfo.split (':')[-2][0:2]
		
			# Calls gene name
			gene = sampleInfo.split (':')[-1]
			
			# Split primerInfo into forward and reverse primers
			fwdPrimer = primerInfo.split ('|')[0]
			revPrimer = primerInfo.split ('|')[2]
		
			# Define the nucleotides to count GC content
			A = seq.count('A')
			G = seq.count('G')
			C = seq.count('C')
			T = seq.count('T')
			GCcontent = (G+C) / (A+G+C+T)
			
			sequenceData[sampleID] = {
				'Technology' : technology,
				'Forward Primer' : fwdPrimer,
				'Reverse Primer' : revPrimer,
				'Gene' : gene,
				'Country' : country,
				'GC content' : GCcontent
				}
			seqDataOutput.write( "technology: %s\tfwdPrimer: %s\trevPrimer: %s\tgene: %s\tcountry: %s\n" % ( technology, fwdPrimer, revPrimer, gene, country))
			
			sequences[sampleID] = seq
		#end For loop
	#close 'Info' file
	
# Determining the length of individual sequences
	Length = [len(v) for v in sequences.values()]

# Using a for loop to determine nucleotide content for each sequence 
	listsequences = []
	for key, value in sequences.items():
		nucs = ['A', 'C', 'T', 'G']
		count = [value.count(x) for x in nucs]
		listsequences.append((count[1]+count[3]) / (count[0]+count[1]+count[2]+count[3]))
		GC = sum(listsequences) / 1753
	
	seqDataOutput.write("Input File: %r\t" % (fasta))
	seqDataOutput.write("Output File: %r\t" % (output))
	seqDataOutput.write("Number of sequences: %d\t" % len(sequences))
	seqDataOutput.write("Average length of sequences: %r\t" % (sum(Length)/1753))
	seqDataOutput.write("Average GC content: %r" % (GC))
#close 'seqDataOutput' file