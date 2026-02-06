def rows(letter):
    dist = ord(letter) - ord('A') #C = 3
    size = 2 * dist + 1 # 5
    result = []

    for i in range(size): # 0 to 4
        # Current row distance from the vertical center
        row_dist = abs(i - dist) 
        char_offset = dist - row_dist
        to_left = dist - char_offset
        to_right = dist + char_offset

        # The character for this row
        current_char = chr(ord('A') + (char_offset))
        
        # Builds the string of fillers first
        row_list = [" "] * size
        
        # Calculate column positions based on symmetry
        # At row_dist from center, the characters are at:
        # center - (dist - row_dist) and center + (dist - row_dist)
        row_list[to_left] = current_char
        row_list[to_right] = current_char
        
        result.append("".join(row_list))
    
    return result
