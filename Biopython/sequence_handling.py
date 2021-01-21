from Bio.Seq import Seq
from collections import Counter

import pprint
import matplotlib.pyplot as plt


# Create a simple sequence object

sequence_dna = Seq("ATCGATCGATCAGTCAGC")
sequence_rna = Seq("AUCGAUCGAUCGAUCGUC")
protein_a = Seq("VVPSPQVQPPAWSSVAAFSHSEL")

# Lenght of Sequences

print(len(sequence_dna), len(sequence_rna), len(protein_a))

# Slice the Sequences

sliced_dna = sequence_dna[0:3]

print(sliced_dna)

# reverse the sequence

reversed_protein = protein_a[::-1]

print(reversed_protein)

# Join Sequences

sequence_dna_2 = Seq("CAGGCAGC")
joined_sequence = sequence_dna + sequence_dna_2

print(joined_sequence)

# Count number of Nucleotides or AminoAcids

u = sequence_rna.count("U")
m = protein_a.count("M")

print(u, m)

# Find the position of the first occurence of a nucleotide or aminoacids

t_position = sequence_dna.find("T")

print(t_position)

# Or

t_position = sequence_dna.index("T")

print(t_position)


# Find the position of the last occurence of a nucleotide or aminoacids

a_position = sequence_dna.rfind("A")

print(a_position)

# Or

a_position = sequence_dna.rindex("A")

print(a_position)

# Get frequencies of nucleotides or aminoacids

dna_frequence = Counter(sequence_dna)
protein_frequence = Counter(protein_a)

print(dna_frequence)
print(protein_frequence)

# Plot in a bar graph the frequences

plt.bar(dna_frequence.keys(), dna_frequence.values())
plt.savefig("dna_plot.png")
plt.close()
plt.bar(protein_frequence.keys(), protein_frequence.values())
plt.savefig("protein_plot.png")
plt.close()