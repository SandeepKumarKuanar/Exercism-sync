#include "binary.h"
#include<string.h>
#include<math.h>
int convert(const char *input){
    // this comes an input like looking like binary string → '101010\0'
    int length = strlen(input);
    int number = 0;
    
    // Check for invalid input
    if (input == NULL || length == 0) {
        return -1;
    }
    
    for(int i = 0; i < length; ++i){
        // Check if character is valid binary digit
        if (input[i] != '0' && input[i] != '1') {
            return -1;  // Invalid binary number
        }
        int bin = input[i] - '0';  // Convert char to int (0 or 1)
        int power = length - 1 - i;  // Calculate exponent
        number += bin * pow(2.0, power);
    }
    return number;
}
