#!/usr/bin/env python3

# User can enter either DNA sequence or RNA sequence.
right_dna = False
while right_dna == False:
    dna_input = input("Enter DNA sequence or RNA sequence: ")

    dna = dna_input.upper()     # converting DNA in uppercase.

    if len(dna) % 3 != 0:
        print("Note : Nucleotides in DNA are not in multiple of 3")    # checking if nucleatides in input DNA are in multiple of three.

    for nt in dna:
        if nt == "A" or nt == "T" or nt == "G" or nt == "C" or nt == "U":
            right_dna = True
            #print ("Dna sequence is incorrect. Please check the nucleotides")
        else:
            print ("Dna sequence is incorrect. Please check the nucleotides")
            right_dna = False
            break


# making a list out of nucleotides in dna_list.
dna_list = []      # Definig DNA list.
for nt in dna:
    dna_list.append(nt)


# Converting DNA to RNA
rna_list = []       # Definig RNA list.

# Converting DNA into RNA by replacing "T" to "U".
for nt in dna_list:
    if nt != "T":
        rna_list.append(nt)
    else :
        rna_list.append("U")

rna = "".join(str(nt) for nt in rna_list)
print("RNA sequence : " + rna)

# Defining codon list having codons.
codon_list0 = []
codon_list1 = []
codon_list2 = []

# Making codons from RNA
# codons 0
for i in range(0, len(rna_list), 3):
    codon = tuple(rna_list[i:i+3])
    codon_list0.append(codon)    # codon_list is a list tupels containig codon, starting from the first codon.
# codons 1
for i in range(1, len(rna_list), 3):
    codon = tuple(rna_list[i:i+3])
    codon_list1.append(codon)    # codon_list is a list tupels containig codon, starting from the seconf codon.
# codons 2
for i in range(2, len(rna_list), 3):
    codon = tuple(rna_list[i:i+3])
    codon_list2.append(codon)    # codon_list is a list tupels containig codon, starting from the third codon.

#print("Codons 0 : " , codon_list0)
#print("Codons 1 : " , codon_list1)
#print("Codons 2 : " , codon_list2)

# Function for converting codons into their protein.
def codon_to_protein(codon_list):
    protein_list = []
    protein_list_final = []

    is_start = False   # Checks if Start codon is presenst.
    is_stop = False    # Checks if Stop codon is present.

    for codon in codon_list:
        if codon == ("U", "U", "U") or codon == ("U", "U", "C"):
            protein_list.append("Phe(F)")
        elif codon == ("U", "U", "A") or codon == ("U", "U", "G"):
            protein_list.append("Leu(L)")
        elif codon == ("U", "C", "U") or codon == ("U", "C", "C") or codon == ("U", "C", "A") or codon == ("U", "C", "G"):
            protein_list.append("Ser(S)")
        elif codon == ("U", "A", "U") or codon == ("U", "A", "C"):
            protein_list.append("Tyr(Y)")
        elif codon == ("U", "G", "U") or codon == ('U', 'G', 'C'):
            protein_list.append("Cys(c)")
        elif codon == ('U', 'G', 'G'):
            protein_list.append("Trp(W)")
        elif codon == ('C', 'U', 'U') or codon == ('C', 'U', 'C') or codon == ('C', 'U', 'G') or codon == ('C', 'U', 'A'):
            protein_list.append("Leu(L)")
        elif codon == ('C', 'C', 'C') or codon == ('C', 'C', 'U') or codon == ('C', 'C', 'G') or codon == ('C', 'C', 'A'):
            protein_list.append("Pro(P)")
        elif codon == ('C', 'A', 'U') or codon == ('C', 'A', 'C'):
            protein_list.append("His(H)")
        elif codon == ('C', 'A', 'A') or codon == ('C', 'A', 'G'):
            protein_list.append("Gln(Q)")
        elif codon == ('C', 'G', 'U') or codon == ('C', 'G', 'G') or codon == ('C', 'G', 'C') or codon == ('C', 'G', 'A'):
            protein_list.append("Arg(R)")
        elif codon == ('A', 'U', 'G'):
            protein_list.append("[START] Met(M)")
        elif codon == ('A', 'U', 'U') or codon == ('A', 'U', 'C') or codon == ('A', 'U', 'A'):
            protein_list.append("Ile(I)")
        elif codon == ('A', 'C', 'U') or codon == ('A', 'C', 'G') or codon ==  ('A', 'C', 'A') or codon ==  ('A', 'C', 'C'):
            protein_list.append("Thr(T)")
        elif codon == ('A', 'A', 'U') or codon == ('A', 'A', 'C'):
            protein_list.append("Asn(N)")
        elif codon == ('A', 'A', 'A') or codon == ('A', 'A', 'G'):
            protein_list.append("Lys(K)")
        elif codon == ('A', 'G', 'U') or codon == ('A', 'G', 'C'):
            protein_list.append("Ser(S)")
        elif codon == ('A', 'G', 'A') or codon == ('A', 'G', 'G'):
            protein_list.append("Arg(R)")
        elif codon == ('G', 'C', 'U') or codon == ('G', 'C', 'G') or codon == ('G', 'C', 'A') or codon == ('G', 'C', 'C'):
            protein_list.append("Ala(A)")
        elif codon == ('G', 'U', 'U') or codon == ('G', 'U', 'C') or codon == ('G', 'U', 'G') or codon == ('G', 'U', 'A'):
            protein_list.append("Val(V)")
        elif codon == ('G', 'A', 'U') or codon == ('G', 'A', 'C'):
            protein_list.append("Asp(D)")
        elif codon == ('G', 'A', 'A') or codon == ('G', 'A', 'G'):
            protein_list.append("Glu(E)")
        elif codon == ('G', 'G', 'G') or codon == ('G', 'G', 'C') or codon == ('G', 'G', 'A') or codon == ('G', 'G', 'U'):
            protein_list.append("Gly(G)")
        elif codon == ('U', 'G', 'A') or codon == ('U', 'A', 'G') or codon == ('U', 'A', 'A'):
            protein_list.append("STOP")

    # To get amino acids from start codon to end codon only

    if "[START] Met(M)" in protein_list:
        is_start = True
    if "STOP" in protein_list:
        is_stop = True

    if is_start == True and is_stop == True:
        start = protein_list.index("[START] Met(M)")
        stop = protein_list.index("STOP")
        print("Note : Sequence has an internal start codon and a stop codon.")
    elif is_start == True and is_stop == False:
        start = protein_list.index("[START] Met(M)")
        stop = len(protein_list)
        print("Note : Sequence has an internal start codon.")
    elif is_start == False and is_stop == True:
        start = 0
        stop = protein_list.index("STOP")
        print("Note : Sequence has an internal stop codon.")
    elif is_start == False and is_stop == False:
        start = 0
        stop = len(protein_list)

    protein_list_final = protein_list[start:stop+1]

    protein = "".join(str(protein) for protein in protein_list_final)

    return protein

# Driver code
protein0 = codon_to_protein(codon_list0)
protein1 = codon_to_protein(codon_list1)
protein2 = codon_to_protein(codon_list2)
print("Protein possibility I : " , protein0)
print("Protein possibility II : " , protein1)
print("Protein possibility III : " , protein2)

# Checking the largest protein out of these three.
protein0_length = len(protein0)
protein1_length = len(protein1)
protein2_length = len(protein2)

if protein0_length > protein1_length and protein0_length > protein2_length:
    final_protein = protein0
    final_protein_prob = "Possibility I"
elif protein1_length > protein0_length and protein1_length > protein2_length:
    final_protein = protein1
    final_protein_prob = "Possibility II"
elif protein2_length > protein0_length and protein2_length > protein1_length:
    final_protein = protein2
    final_protein_prob = "Possibility III"

print("The largest of the three possible proteins is  {} ".format(final_protein_prob))
print("\n \n \t \tSo, the most probable protein outcome is \" {} \" ".format(final_protein))
