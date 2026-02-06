def proteins(strand):
    def chunk_string(s, size):
        """Yield successive n-sized chunks from s."""
        for i in range(0, len(s), size):
            yield s.upper()[i:i + size]
    ### using the chunking function here
    strand_list = list(chunk_string(strand, 3))
    protein_strand = []
    for codon in strand_list:
        if codon == "AUG":
            protein_strand.append("Methionine")
        elif codon == "UUU" or codon == "UUC":
            protein_strand.append("Phenylalanine")
        elif codon == "UUA" or codon == "UUG":
            protein_strand.append("Leucine")
        elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
            protein_strand.append("Serine")
        elif codon == "UAU" or codon == "UAC":
            protein_strand.append("Tyrosine")
        elif codon == "UGU" or codon == "UGC":
            protein_strand.append("Cysteine")
        elif codon == "UGG":
            protein_strand.append("Tryptophan")
        elif codon == "UAA" or codon == "UAG" or codon == "UGA":
            break
    return protein_strand
    