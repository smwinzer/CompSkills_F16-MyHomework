#Solution for HW4, will extract information about DNA sequences from a fasta file

import sys

#Read from STDIN

Headers = sys.stdin.readlines()
#Seqs = ">MISEQ:7:000000000-AMAKG:1:1101:16998:1719 1:N:0:PE716:ST6_21 TTGACCCT|0|TAGACCTA|0 ST6_21_F|0|23|"

#Split each line input into separate fields

for nextHeader in Headers:
    Fields = nextHeader.split(" ")
    Technology, sampleID, Primers, gene = Fields
	
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
	
	#print all fields separated by tabs
	print("SampleID: %s\tTech: %s\tfwd: %s\trev: %s\tGene: %s\tOrigin: %s\n" % (sampleID,Technology,fwdPrimer,revPrimer,gene,Origin))