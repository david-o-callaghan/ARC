"""
Author: Keith Daly
"""


import solver_utils
import numpy as np
import itertools


def solve(input_grid):
    """
    This function contains a solution to the data in beb8660c.json posed by the Abstraction and 
    Reasoning Corpus (ARC).
    
    The problem presents an n x m grid, with some rows containing 0-m coloured squares with no repetition. 
    The solution requires the rows to be ordered such that the row with m coloured squares is row n, the row 
    with m-1 coloured squares is row n-1, etc. Another stipulation is that the coloured squares start from the 
    right such that in row n-1, column 0 is coloured black and in row n-2, column 0 and 1 are coloured black, etc.
    
    Input: input_grid - A python list of lists containing the unsolved grid
    
    Output: out_grid - A python list of lists containing the solved grid
    
    """
    # Change grid to NumPy array
    np_grid = np.array(input_grid)
    out_grid = np.zeros_like(np_grid)
    
    # Extract number of rows and columms
    numRows, numCols = np_grid.shape
    
    # Dict to store rows with num of colours in each row
    rowsWithNumColours = {row: 0 for row in range(numRows)}
    # Dict to store the colour for the row
    rowColour = {row: 0 for row in range(numRows)}
    
    # Checking for rows with coloured squares, storing colour & number of coloured squares
    for i, j in itertools.product(range(numRows), range(numCols)):
        if np_grid[i, j] != 0:
                rowsWithNumColours[i] += 1
                rowColour[i] = np_grid[i, j]
                
    # Dict sorted by value 
    # Source https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    # Accessed 17/11/2019
    sortedRows = sorted(rowsWithNumColours.items(), key=lambda x: x[1])
    
    # Count for row in output grid
    rowCount = 0
    
    for pair in sortedRows:
        # Row number and number of coloured squares in the row
        row, num = pair
        # Skip rows that have no coloured squares
        if(num == 0):
            rowCount += 1
            continue
        # Colour starts at the end of row, using negative indexing to colour correct squares
        num = -1 * num
        while(num < 0):
            # Get colour corresponding to the row 
            colour = rowColour[row] 
            # Set output grid squares to correct colour
            out_grid[rowCount, num] = colour
            num += 1
        rowCount += 1
        
    return out_grid.tolist()
    
    
if __name__ == "__main__":
    data = solver_utils.parse_json_file()
    
    for training in data['train']:
        solver_utils.solve_wrapper(training['input'], solve)
        
    for testing in data['test']:
        solver_utils.solve_wrapper(testing['input'], solve)