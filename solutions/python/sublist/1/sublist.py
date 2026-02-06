"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0
def check_sublist(source, target):    
    len_s, len_t = len(source), len(target)
    if len_s > len_t:
        return False
    return any(target[i : i + len_s] == source for i in range(len_t - len_s + 1))
def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if check_sublist(list_one, list_two):
        return SUBLIST
    if check_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL