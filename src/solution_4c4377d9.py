# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:43:04 2019

@author: Ajinkya Sakhare
"""
import solver_utils
import numpy as np

def solve(inputmatrix):
    y = np.array(inputmatrix)
    y_copy=y
    y=y[[2,1,0], :]
    return((np.concatenate((y, y_copy))).tolist())

# Use main() from solution_4be741c5.py as template
if __name__ == "__main__":
    data = solver_utils.parse_json_file()

    for training in data['train']:
        solver_utils.solve_wrapper(training['input'], solve)

    for testing in data['test']:
        solver_utils.solve_wrapper(testing['input'], solve)