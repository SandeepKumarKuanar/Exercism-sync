def append(list1, list2):
    return list1 + list2


def concat(lists):
    flattened_list = [item for sublist in lists for item in sublist]
    return flattened_list


def filter(function, list):
    return [element for element in list if function(element)]


def length(list):
    return len(list)


def map(function, list):
    return [function(element) for element in list]


def foldl(function, list, initial):
    acc = initial
    
    for element in list:
        # We update the state by applying the function to the current state and the element
        acc = function(acc, element)
        
    return acc


def foldr(function, list, initial):
    acc = initial
    
    # CRITICAL CHANGE: We iterate the list in reverse order (Right-to-Left)
    for element in reversed(list):
        acc = function(acc, element)
        
    return acc


def reverse(list):
    return list[::-1]
