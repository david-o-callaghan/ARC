"""
Author: David O'Callaghan
"""

import numpy as np
import solver_utils

def solve(grid_in):
    """
    This function contains the hand-coded solution for the data in 
    5c0a986e.json of the Abstraction and Reasoning Corpus (ARC)

    Transformation Description: The input grid for this problem always 
    contains one blue and one red 2-by-2 square. The transformation to change 
    the colour of the elements that connect the top-left corner of the blue 
    square to the grid-boundary in the North-West direction to blue and the 
    elements that connect the bottom-right corner of the red square to the 
    grid-boundary in the South-East direction to red. 
    
    Inputs: grid_in - A python list of lists containing the unsolved grid data
    
    Returns: grid_out - A python list of lists containing the solved grid data
    """
    # Convert to numpy array
    grid_in_np = np.array(grid_in)
    
    # Create output grid with same data as input grid
    grid_out_np = np.copy(grid_in_np)
    
    # Get index of colour (to improve readability)
    blue = solver_utils.get_colour_code('blue')
    red = solver_utils.get_colour_code('red')
    
    # Used to check if task completed later
    blue_done = False
    red_done = False
    
    # Iterate through the elements in the grid (row by row)
    n_rows, n_cols = np.shape(grid_out_np)
    for i in range(n_rows):
        for j in range(n_cols):
            # Check if pixel is blue
            if grid_in_np[i,j] == blue and not blue_done:
                # Top left corner of square hit
                m, n = i, j
                # Change colours diagonally towards North-West
                while m > 0 and n > 0:
                    m -= 1
                    n -= 1
                    grid_out_np[m,n] = blue
                blue_done = True

            # Check if pixel is red
            if grid_in_np[i,j] == red and not red_done:
                # Go to bottom right corner of square
                m, n = i+1, j+1
                # Change colours diagonally towards South-East
                while m < n_rows-1 and n < n_cols-1:
                    m += 1
                    n += 1
                    grid_out_np[m,n] = red
                red_done = True
            
            # No need to keep iterating if tasks are done
            if blue_done and red_done:
                break
    
    # Convert back to list of lists
    grid_out = grid_out_np.tolist()
    
    return grid_out

if __name__=='__main__':
    # Get the data for the associated JSON file
    data = solver_utils.parse_json_file()
    
    # Iterate through training grids and test grids
    for data_train in data['train']:
        solver_utils.solve_wrapper(data_train['input'], solve)
        
    for data_test in data['test']:
        solver_utils.solve_wrapper(data_test['input'], solve)
 
