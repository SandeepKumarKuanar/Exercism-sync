def tick(matrix):
    if len(matrix) == 0:
        return matrix
    ROWS, COLS = len(matrix), len(matrix[0])

    def count_neighbors(r, c):
        neighbor = 0
        for row in range(r - 1, r + 2):
             for column in range(c - 1, c + 2):
                 if(row == r and column == c) or row < 0 or column < 0 or row == ROWS or column == COLS:
                     continue
                 if matrix[row][column] in [1, 3]:
                     neighbor += 1
        return neighbor
    
    for row in range(ROWS):
        for column in range(COLS):
            neighbor = count_neighbors(r=row, c=column)
            if matrix[row][column]:
                if neighbor in [2, 3]:
                    matrix[row][column] = 3
            else:
                if neighbor == 3:
                    matrix[row][column] = 2
    
    for row in range(ROWS):
        for column in range(COLS):
            if matrix[row][column] == 1:
                matrix[row][column] = 0    
            elif matrix[row][column] in [2, 3]:
                matrix[row][column] = 1 

    return matrix