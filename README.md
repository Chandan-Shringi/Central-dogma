# Central-dogma
Program to convert DNA into RNA and then Protein (amino acids). 

This program takes a DNA or RNA string as input.
If DNA sequence is given as input, converts the DNA sequence into its corrosponding RNA sequence \(i.e. by changing 'T' to 'U' \).

#### Protein sequence
This program then converts the RNA sequence into the corrosponding amino acids sequence by following the rule of codons.
* If start codon is present in the sequence,the translation will start from there and thus codons before the start codon will not reflect on the final protein \(amino acids sequence \).
* Simmilarly, if stop codon is present in between, the translation will stop there and the codons after stop codon will no reflect in final protein \(amino acids sequence \).
* If no start codon or stop codon is present in the RNA sequence, the complete RNA sequence get translated into corrosponding amino acid sequence. 
