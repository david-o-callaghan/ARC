# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:43:04 2019

@author: Ajinkya Sakhare
"""
import numpy as np
import solver_utils

def solve(inputmatrix):
    """
        This function contains a solution to the data in 4be741c5.json posed by the Abstraction and
        Reasoning Corpus (ARC).

        The problem presents an n x m grid, with some rows containing 0-m coloured squares with repetition over a row or colomuns.
        The solution requires the rows to be ordered such that it get color of all unique colors if it is either row-wise or colomun-wise.
    """
    #Empty result list to return results
    result=[]
    #convert input to numpy array

    y = np.array([np.array(xi) for xi in inputmatrix])

    if len(np.unique(y[:1][0]))>1:#if the count of unique colors is more than one

        indexes = np.unique(y[:1][0], return_index=True)[1] #Get the indexes of unique colour
        row=[y[:1][0][index] for index in sorted(indexes)]#Get the unique colors in unsorted list
        result.append(row)#append row to result

    else:#if colour are in colomun
        indexes = np.unique(y[:, 0], return_index=True)[1]#Get the indexes of unique colour
        colomun = [y[:, 0][index] for index in sorted(indexes)]#Get the unique colors in unsorted list
        for value in colomun:
            result.append([value])#Appending values to the result
    return (result)

if __name__ == "__main__":
    data = solver_utils.parse_json_file()

    for training in data['train']:
        solver_utils.solve_wrapper(training['input'], solve)

    for testing in data['test']:
        solver_utils.solve_wrapper(testing['input'], solve)
