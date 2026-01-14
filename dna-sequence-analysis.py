# DNA Sequence Analysis Toolkit

# This program performs basic DNA sequence analysis

# -------------------------------
# Function to validate DNA
# -------------------------------
def validate_dna(sequence):
    sequence = sequence.upper()
    for base in sequence:
        if base not in "ATGC":
            return False
    return True


# -------------------------------
# Nucleotide count
# -------------------------------
def nucleotide_count(sequence):
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }


# -------------------------------
# GC Content calculation
# -------------------------------
def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    return ((g + c) / len(sequence)) * 100


# -------------------------------
# Reverse Complement
# -------------------------------
def reverse_complement(sequence):
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    rev_comp = "".join(complement[base] for base in reversed(sequence))
    return rev_comp


# -------------------------------
# Transcription (DNA -> RNA)
# -------------------------------
def transcription(sequence):
    return sequence.replace("T", "U")


# -------------------------------
# Translation (DNA -> Protein)
# -------------------------------
def translation(sequence):
    codon_table = {
        "ATA":"I","ATC":"I","ATT":"I","ATG":"M",
        "ACA":"T","ACC":"T","ACG":"T","ACT":"T",
        "AAC":"N","AAT":"N","AAA":"K","AAG":"K",
        "AGC":"S","AGT":"S","AGA":"R","AGG":"R",
        "CTA":"L","CTC":"L","CTG":"L","CTT":"L",
        "CCA":"P","CCC":"P","CCG":"P","CCT":"P",
        "CAC":"H","CAT":"H","CAA":"Q","CAG":"Q",
        "CGA":"R","CGC":"R","CGG":"R","CGT":"R",
        "GTA":"V","GTC":"V","GTG":"V","GTT":"V",
        "GCA":"A","GCC":"A","GCG":"A","GCT":"A",
        "GAC":"D","GAT":"D","GAA":"E","GAG":"E",
        "GGA":"G","GGC":"G","GGG":"G","GGT":"G",
        "TCA":"S","TCC":"S","TCG":"S","TCT":"S",
        "TTC":"F","TTT":"F","TTA":"L","TTG":"L",
        "TAC":"Y","TAT":"Y","TAA":"_","TAG":"_",
        "TGC":"C","TGT":"C","TGA":"_","TGG":"W"
    }

    protein = ""
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        protein += codon_table.get(codon, "X")
    return protein


# -------------------------------
# Main Program
# -------------------------------
def main():
    print("🧬 DNA Sequence Analysis Toolkit")
    print("-" * 35)

    dna = input("Enter DNA sequence: ").upper()

    if not validate_dna(dna):
        print("❌ Invalid DNA sequence! Use only A, T, G, C.")
        return

    print("\n✅ Sequence Accepted")
    print(f"Sequence Length: {len(dna)} bp")

    counts = nucleotide_count(dna)
    print("\nNucleotide Count:")
    for base, count in counts.items():
        print(f"{base}: {count}")

    print(f"\nGC Content: {gc_content(dna):.2f}%")
    print(f"\nReverse Complement:\n{reverse_complement(dna)}")
    print(f"\nTranscribed RNA:\n{transcription(dna)}")
    print(f"\nTranslated Protein:\n{translation(dna)}")


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()
