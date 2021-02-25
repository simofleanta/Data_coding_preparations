"""sudoku"""

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c


    return None,None  #if there are no empty spaces in the puzzle (-1)

def valid_guess(puzzle, guess, row,col):
    #if the guess in the row and col are valid; True if valid, false otherwise
    #start with row:
    row_value=puzzle[row]
    if guess in row_value:
        return False
    #no col:
    col_value=[]
    for i in range(9):
        col_value.append(puzzle[i][col])
    col_value=[puzzle[i][col] for i in range(9)]
    if guess in col_value:
        return False

    
    #the square
    row_start=(row//3) *3  #1//3=0, 5//3=1, ...
    col_start=(col//3) *3 

    for r in range(row_start , row_start + 3):
        for c in range (col_start, col_start +3):
            if puzzle[r][c]==guess:
                return False

    #if values pass checks

    return True


def sudoku (puzzle):
    #use backtracking to solve the sudoku p
    # puzzle is a list of lists where each inner list is a row in the sudoku puzzle.
    # return return whther a solution exists.
    #if there is a solution mutate puzzle to be a solution
    # will do it in steps
#step1
    row,col=find_next_empty(puzzle)

#step 1.1:  if there's no where  left, then there's nothing much to do as we only alow valid inputs.

    if row is None:
        return True

# step 2: if there is a space to place guess, then make the guess btw 1-9
    
    for guess in range(1,10):
        #step 3
        if valid_guess(puzzle, guess, row,col):
            #step 3.1 : if this is valid add row to column.
            puzzle[row][col] = guess
            # no recurse usinf this puzzle:
            #step 4 : recursively call function
            if sudoku(puzzle):
                return True
            
            #step 5 : if not vald or if sufoku does not solve, ned to backtrack reset and move to next guess
            puzzle[col]= -1 #reset guess

            # step 6: if unsolvable return f
            return False

if __name__== '__main__':
    sudoku_board=[

        [3, 9, -1,   -1, 5, -1, -1,-1,-1],
        [-1, -1, -1,  2,-1, -1, -1,-1,5 ],
        [-1, -1, -1,  7, 1, 9,  -1, 8, -1],
         
        [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
        [2, -1, 6,   -1,-1, 3,  -1, -1, -1],
        [-1, -1,-1,  -1,-1, -1, -1,-1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1,   1, -1, 5,  -1, 4, -1],
        [1, -1, 6,  -1,-1,-1,    2, -1,-1]
    ]
    print(sudoku(sudoku_board))
    print(sudoku_board)















