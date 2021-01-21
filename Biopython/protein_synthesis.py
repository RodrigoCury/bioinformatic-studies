from Bio.Seq import Seq
import pprint

sequence_dna = Seq("ATCGATCGATCAGTCAGCTGA")

# DNA Methods

dna_complement = sequence_dna.complement()
dna_reverse_complement = sequence_dna.reverse_complement()
rna_transbribed_from_dna = sequence_dna.transcribe()
protein_translated_from_dna = sequence_dna.translate()
# Custom Stop Codon Symbol
protein_translated_from_dna_other_stop = sequence_dna.translate(stop_symbol=" stop ")

pprint.pprint(
    [
        sequence_dna,
        dna_complement,
        dna_reverse_complement,
        rna_transbribed_from_dna,
        protein_translated_from_dna,
        protein_translated_from_dna_other_stop,
    ]
)

# RNA methods

messenger_rna = Seq("UUGCAUGCAGCACGAACGUGA")

dna_back_transcribed = messenger_rna.back_transcribe()
protein_translated_from_rna = messenger_rna.translate()

pprint.pprint([messenger_rna, dna_back_transcribed, protein_translated_from_rna])

# Protein Methods
from Bio.SeqUtils import seq1, seq3

protein_sequence = Seq("MIDRSVS*")

protein_tree_letters = seq3(protein_sequence)
protein_back_one_letter = seq1(protein_tree_letters)

pprint.pprint([protein_sequence, protein_tree_letters, protein_back_one_letter])

# View Codon Table

from Bio.Data import CodonTable

print(CodonTable.ambiguous_dna_by_name["Standard"])