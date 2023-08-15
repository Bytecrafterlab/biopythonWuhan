from Bio import SeqIO
from Bio.Seq import Seq

# Read DNA sequence from a file
def read_sequence_from_file(file_path):
    with open(file_path, "r") as file:
        sequence_record = SeqIO.read(file, "fasta")
        return sequence_record.seq

# Calculate GC content
def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_bases = len(sequence)
    gc_content = (gc_count / total_bases) * 100
    return gc_content

# Reverse complement the sequence
def reverse_complement(sequence):
    reverse_seq = sequence.reverse_complement()
    return reverse_seq

# Main function
def main():
    input_file = "wuhan.fasta"  # Replace with your input file name

    # Read sequence from file
    dna_sequence = read_sequence_from_file(input_file)

    # Calculate GC content
    gc_content = calculate_gc_content(dna_sequence)
    print(f"GC content: {gc_content:.2f}%")

    # Reverse complement the sequence
    reversed_sequence = reverse_complement(dna_sequence)
    print("Original Sequence:")
    print(dna_sequence)
    print("\nReversed Complement:")
    print(reversed_sequence)

if __name__ == "__main__":
    main()
