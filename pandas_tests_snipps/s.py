"""sudoku"""

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c


    return None,None  #if there are no empty spaces in the puzzle (-1)

def valid_guess(puzzle, guess, row,col):
    pass
    


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

# if there is a space to place guess, then make the guess btw 1-9
    
    for guess in range(1,10):
        #step 3
        if valid_guess(puzzle, guess, row,col):









