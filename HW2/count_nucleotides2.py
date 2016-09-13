# This is the python code for homework assignment #2
# This code is not yet completed. It is due by midnight Thursday 9/15
'''
Todo:
1. Input two nucleotide sequences as strings into variables with meaningful names
	sequence 1: CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA (52 nucleotides)
	sequence 2: CGGATCGTAAAGCTCTGTTGTTGGTGAAGAAGGATAGAGGTAGTAACTGGCCT (53 nucleotides)
2. Count the number of each nucleotide in a sequence
3. Determine the GC content of each sequence
	GC content is determined by the number of G's plus the number of C's divided by the 
	sequence length, but double check this...
4. Print the following:
		sequence: *sequence*
		A's: *number of A's*
		C's:
		T'S:
		G's:
		GC content: *gc content*
5. Redirect file output into ncounts.txt (this will be done on the command line)
'''


#Inputing sequences into strings

sequence1="CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA"
sequence2="CGGATCGTAAAGCTCTGTTGTTGGTGAAGAAGGATAGAGGTAGTAACTGGCCT"

#Count the number of each nucleotide in each sequence

NumA1=sequence1.count("A")
NumC1=sequence1.count("C")
NumT1=sequence1.count("T")
NumG1=sequence1.count("G")

NumA2=sequence2.count("A")
NumC2=sequence2.count("C")
NumT2=sequence2.count("T")
NumG2=sequence2.count("G")

#Determine the GC content of each sequence

GC1 = ( NumC1 + NumG1 ) / 52

GC2 = ( NumC2 + NumG2 ) / 53

#Print the information

print("sequence: " , sequence1)
print("A's: " , NumA1)
print("C's: " , NumC1)
print("T's: " , NumT1)
print("G's: " , NumG1)
print("GC content: " , GC1)

print("sequence: " , sequence2)
print("A's: " , NumA2)
print("C's: " , NumC2)
print("T's: " , NumT2)
print("G's: " , NumG2)
print("GC content: " , GC2)

