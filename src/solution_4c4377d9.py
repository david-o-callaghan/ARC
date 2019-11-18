# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:43:04 2019

@author: Ajinkya Sakhare
"""
import solver_utils
import numpy as np

def solve(inputmatrix):
    """
            This function contains a solution to the data in 4be741c5.json posed by the Abstraction and
            Reasoning Corpus (ARC).

            The problem presents an n x m grid, with some rows containing 0-m coloured squares with repetition over a row or colomuns.
            The solution requires the same colour pattern to be first mirrored and then concatenated with the older pattern. which
            in result will create a grid of n x2m.
        """
    y = np.array(inputmatrix)#convert input matrix to numpy array
    y_copy=y#Make a copy of existing pattern
    y=y[[2,1,0], :]#swap first and last rows with each other
    return((np.concatenate((y, y_copy))).tolist())#return a concatinated mirrored matrix to the old stored in y_copy

# Use main() from solution_4be741c5.py as template
if __name__ == "__main__":
    data = solver_utils.parse_json_file()

    for training in data['train']:
        solver_utils.solve_wrapper(training['input'], solve)

    for testing in data['test']:
        solver_utils.solve_wrapper(testing['input'], solve)