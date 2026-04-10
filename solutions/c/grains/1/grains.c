#include "grains.h"
#include <math.h>
uint64_t square(uint8_t index) {
    // Invalid index
    if (index < 1 || index > 64) {
        return 0;
    }
    
    // 1 << (index - 1) is 2^(index-1)
    // Need to cast to uint64_t before shifting
    return 1ULL << (index - 1);
}

uint64_t total(void) {
    // Total = 2^64 - 1
    // Using ULL suffix for unsigned long long
    return 18446744073709551615ULL;
    
    // Alternative: calculate it
    // return ~0ULL;  // Bitwise NOT of 0 gives all 1s = 2^64 - 1
}