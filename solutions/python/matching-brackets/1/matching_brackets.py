def is_paired(input_string):
    bracket_map = {
        "]": "[", 
        "}": "{", 
        ")": "(",
    }
    stack = [] #Last in first out method 
    for char in input_string:
        if char in ["[", "{", "("]:
            stack.append(char)
        elif char in bracket_map:
            if not stack:
                return False
            last_opened = stack.pop()
            if last_opened != bracket_map[char]:
                return False
    return len(stack) == 0
        