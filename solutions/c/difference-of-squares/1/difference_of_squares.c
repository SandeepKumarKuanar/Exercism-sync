#include "difference_of_squares.h"
unsigned int sum_of_squares(unsigned int number){
    unsigned int want = 1;
    for(unsigned int i = number; i > 1; i--){
        want += i * i;
    }
    return want;
}
unsigned int square_of_sum(unsigned int number){
    unsigned int want = 1;
    for(unsigned int i = number; i > 1; i--){
        want += i;
    }
    return want * want;
}
unsigned int difference_of_squares(unsigned int number){
    return square_of_sum(number) - sum_of_squares(number);
}