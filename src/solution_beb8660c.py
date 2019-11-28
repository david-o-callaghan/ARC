# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:43:04 2019

@author: Keith Daly
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
    
    """
    # Change grid to NumPy array
    np_grid = np.array(input_grid)
    
    
    # Sort rows relative to eachother based on how many zeros they contain
    # Source: https://stackoverflow.com/questions/28518568/numpy-sort-matrix-rows-by-number-of-non-zero-entries
    # Accessed 23/11/2019
    np_grid = np_grid[(np_grid != 0).sum(axis=1).argsort()]
    # Sort entries in each row
    np_grid.sort(axis=1)
        
    return np_grid.tolist()
    
    
if __name__ == "__main__":
    data = solver_utils.parse_json_file()
    
    for training in data['train']:
        solver_utils.solve_wrapper(training['input'], solve)
        
    for testing in data['test']:
        solver_utils.solve_wrapper(testing['input'], solve)