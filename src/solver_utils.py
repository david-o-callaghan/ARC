import argparse
import json

def print_grid(grid_in):
    """
    Prints the elements of grid_in with a space between each element along the
    columns and a new line for each row. Assumes that grid_in is a list of
    lists.
    """
    #iterate through grid
    for row in grid_in:
        for elem in row:
            # print element followed by space
            print(elem, end=' ') 
        print() # go to new line

def solve_wrapper(data_in, solver):
    """
    Calls the solver function on data_in and calls print_grid on the result.
    """
    # Call the solver function
    data_out = solver(data_in)    
    
    # Print the results
    print_grid(data_out)
    print()
    
def get_colour_code(colour):
    """
    This function returns the integer associated with the input string for the
    ARC problems.
    """
    colour_mapping = {'black':0,
                      'blue':1,
                      'red':2,
                      'green':3,
                      'yellow':4,
                      'grey':5,
                      'pink':6,
                      'orange':7,
                      'babyblue':8,
                      'maroon':9}
    
    return colour_mapping[colour]
 
def parse_json_file():
    """
    This function reads the data from the JSON file passed from the command
    line and returns the data after converting it to a Python dictionary.
    """
    # Get file name passed from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_json")
    args = parser.parse_args()
    
    # Read file as text
    with open(args.input_file_json) as f:
        text = f.read()
        
    # Return JSON data as Python dictionary    
    return json.loads(text)
