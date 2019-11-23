import unittest
import json

import solution_5c0a986e
import solution_b91ae062
import solution_2dc579da
import solution_4be741c5
import solution_4c4377d9
import solution_beb8660c
import solution_bd4472b8

# Source https://docs.python.org/3/library/unittest.html
#        [Accessed: 16/11/2019]

class TestSolveFunctions(unittest.TestCase):

    def load_json_data(self, file_name):
        # Read the JSON file
        with open(file_name) as f:
            text = f.read()
    
        # Convert from JSON to Python Dictionary
        return json.loads(text)
    
    def check_solve_function(self, file_name, solve):
        # Load the data from the JSON file
        data = self.load_json_data(file_name)
        
        # Iterate through train and test grids and test that the 
        # solve() function returns the correct output grid
        for data_train in data['train']:
            solution = solve(data_train['input'])
            self.assertEqual(solution, data_train['output'])
        
        for data_test in data['test']:
            solution = solve(data_test['input'])
            self.assertEqual(solution, data_test['output'])
    
    def test_5c0a986(self):
        file_name = '../data/training/5c0a986e.json'
        self.check_solve_function(file_name, solution_5c0a986e.solve)
        
    def test_b91ae062(self):
        file_name = '../data/training/b91ae062.json'
        self.check_solve_function(file_name, solution_b91ae062.solve)
    
    def test_2dc579da(self):
        file_name = '../data/training/2dc579da.json'
        self.check_solve_function(file_name, solution_2dc579da.solve)
    
    def test_4be741c5(self):
        file_name = '../data/training/4be741c5.json'
        self.check_solve_function(file_name, solution_4be741c5.solve)
    
    def test_4c4377d9(self):
        file_name = '../data/training/4c4377d9.json'
        self.check_solve_function(file_name, solution_4c4377d9.solve)
    
    def test_beb8660c(self):
        file_name = '../data/training/beb8660c.json'
        self.check_solve_function(file_name, solution_beb8660c.solve)
    
    def test_bd4472b8(self):
        file_name = '../data/training/bd4472b8.json'
        self.check_solve_function(file_name, solution_bd4472b8.solve)
        
        
if __name__ == '__main__':
    unittest.main()
