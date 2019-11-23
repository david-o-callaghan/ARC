# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:43:04 2019

@author: Ajinkya Sakhare
"""
import solver_utils
import numpy as np

def solve(inputmatrix):
    """
    This function contains a solution to the data in 4be741c5.json posed by the 
    Abstraction and Reasoning Corpus (ARC).

    The problem presents an n-by-m grid. The solution requires the same colour 
    pattern as the input to be mirrored and then concatenated with the original
    pattern. This results in an output grid of n-by-2m.
    """
    
    y = np.array(inputmatrix) # convert input matrix to numpy array
    y_mirrored = np.flip(y, axis=0) # swap first and last rows with each other
    
    # return a concatinated mirrored matrix to the old stored in y_copy
    return np.concatenate((y_mirrored, y)).tolist() 

if __name__=='__main__':
    # Get the data for the associated JSON file
    data = solver_utils.parse_json_file()
    
    # Iterate through training grids and test grids
    for data_train in data['train']:
        solver_utils.solve_wrapper(data_train['input'], solve)
        
    for data_test in data['test']:
        solver_utils.solve_wrapper(data_test['input'], solve)