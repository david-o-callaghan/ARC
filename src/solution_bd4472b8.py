# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 09:07:07 2019

@author: keith
"""

import numpy as np
import solver_utils

def solve(input_grid):
    '''
    This function contains a solution to the data contained in bd4472b8.json posed by the Abstract
    Reasoning Corpus (ARC).
    
    The problem presents an m x n grid, with row one consisting of n colours and row two consisting of
    the colour grey. The solution requires that starting from row three, each row should contain the colour
    of the columns in row one and cycle through these colours until the bottom of the grid is reached. For
    example, in a 10 x 2 grid, with the colours red and green in row one respectively, row three will be 
    coloured red, row four will be coloured green, etc. 
    '''
    # Convert grid to NumPy array
    np_grid = np.array(input_grid)
    
    numRows, numCols = np_grid.shape
        
    # Colours needed for each row after row three
    colours = np_grid[0]
    
    # Start on third row
    row = 2
    
    # Start on first colour
    colour = 0
    
    while(row < numRows):
        # Get colour corresponding to correct row
        rowColour = colours[colour]
        # Add row containing correct colour to input array (each row being altered contains 0s)
        np_grid[row] += np.full_like(np_grid[row], rowColour)
        row += 1
        # Modulus operator to cycle through columns
        colour = (colour + 1) % numCols
        
    return np_grid.tolist()
    
if __name__ == "__main__":
    
    data = solver_utils.parse_json_file()
    
    for training in data['train']:
        solver_utils.solve_wrapper(training['input'], solve)
        
    for testing in data['test']:
        solver_utils.solve_wrapper(testing['input'], solve)