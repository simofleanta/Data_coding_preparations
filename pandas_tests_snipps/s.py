"""sudoku"""

def find_next_empty(puzzle):
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






