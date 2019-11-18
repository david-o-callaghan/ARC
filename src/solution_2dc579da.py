"""
Author: David O'Callaghan
"""

import numpy as np
import solver_utils

def solve(grid_in):
    """
    This function contains the hand-coded solution for the data in 
    2dc579da.json of the Abstraction and Reasoning Corpus (ARC)

    Transformation Description: The center row and center column of the input 
    grid are a different colour to the rest of the grid, effectively dividing 
    the grid into 4 quadrants. One of the 4 quadrants contains an element with 
    a different colour to every other element. The transformation is to select 
    this quadrant as the output grid. 
    
    Inputs: grid_in - A python list of lists containing the unsolved grid data
    
    Returns: grid_out - A python list of lists containing the solved grid data
    """
    # Convert to numpy array
    grid_in_np = np.array(grid_in)
    
    # Find the center index
    midpoint = grid_in_np.shape[0] // 2
    
    # Source : https://stackoverflow.com/questions/6252280/find-the-most-frequent-number-in-a-numpy-vector
    #          [Accessed: 14/11/2019]
    (values,counts) = np.unique(grid_in_np, return_counts=True)
    ind = np.argmin(counts)
    minority_colour = values[ind]
    
    squares = [
            grid_in_np[0:midpoint,0:midpoint],    # Top-left
            grid_in_np[midpoint+1:,0:midpoint],   # Bottom-left
            grid_in_np[0:midpoint,midpoint+1:],   # Top-right
            grid_in_np[midpoint+1:,midpoint+1:]   # Bottom-right
            ]
    
    for square in squares:
        if minority_colour in square:
            grid_out_np = square
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
    
