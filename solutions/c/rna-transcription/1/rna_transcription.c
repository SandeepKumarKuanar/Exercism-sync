#include "rna_transcription.h"
#include<string.h>
#include <stdlib.h>
char *to_rna(const char *dna){
    int length = strlen(dna);
    char *rna = malloc(length + 1);
    if (rna == NULL) {
        return NULL;  // Allocation failed
    }
    for(int i = 0; i < length; ++i){
        if(dna[i] == 'G'){
            rna[i] = 'C';
        }else if(dna[i] == 'C'){
            rna[i] = 'G';
        }else if(dna[i] == 'T'){
            rna[i] = 'A';
        }else if(dna[i] == 'A'){
            rna[i] = 'U';
        }
    }
    rna[length] = '\0'; // Add null terminator
    return rna;
}