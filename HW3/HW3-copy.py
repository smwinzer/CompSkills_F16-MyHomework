#!/usr/bin/env python3.5

#This is the python code for homework 3

'''
This program defines a function CountNucs to count the number of nucleotides within 
a DNA sequence if given said sequence and a list of nucleotides to count. It will 
count the number of ambiguity codes, but only if ATCG are listed first. 
'''

Seq1 = "CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA"
Seq2 = "CGGATCGTAAAGCTCTGTTGTTGGTGAAGAAGGATAGAGGTAGTAACTGGCCT"

Nucs = ["A" , "C" , "G" , "T" , "N" , "Y" , "U"]

'''
def CountNucs( str , char ): 
    for c in s:
        n = 0
        if char == c: 
            n = n + 1
    print(n)
'''

def CountNucs( seq , nucs ): 
    Counts = []
    for nextNuc in nucs:
        Counts.append(seq.count(nextNuc))
    return Counts

    
print(CountNucs(Seq1,Nucs))
print(CountNucs(Seq2,Nucs))

def CountNucs( seq , nucs ): 
    print("Sequence: " , seq)
    Counts = []
    i = -1
    for nextNuc in nucs:
        i = i + 1
        Counts.append(seq.count(nextNuc))
        print(nucs[i] , " occurs " , Counts[i] , "times")
    n = 0
    a = 0
    for nextNuc in seq:
        n = n + 1
        if nextNuc == "N":
        	a = a + 1
        elif nextNuc == "U":
            a = a + 1
        elif nextNuc == "Y":
            a = a + 1
    p = a / n * 100
    print("The sequence has " , n , "nucleotides, where " , a , "(" , p , " %) " "are ambiguous.")
        
CountNucs(Seq1,Nucs)
print()
CountNucs(Seq2,Nucs)









'''
def CountNucs( seq ): 
    totalA = 0
    totalC = 0
    totalG = 0
    totalT = 0
    totalN = 0
    totalY = 0
    totalU = 0
    for char in seq:
        if char == "A":
        	totalA += 1
        elif char == "C":
        	totalC += 1
        elif char == "G":
        	totalG += 1
        elif char == "T":
        	totalT += 1
        elif char == "N":
        	totalN += 1
        elif char == "Y":
        	totalY += 1
        elif char == "U":
        	totalU += 1
'''    