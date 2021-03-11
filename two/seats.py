#!/usr/bin/env python3

import sys
from os.path import dirname, join

# Parsing all the input data 
def parse_testcases(io):
    # Read the number of test cases
    T = int(io.readline())
    tc = []

    # For each test case
    for _ in range(T):
        # Read the input data
        (a, b) = map(int, io.readline(  ).strip().split())
        # Add to the list fo test cases
        tc.append((a,b))

    # Return all the test cases parsed
    return tc

# Function to solve a single test case
def solve_testcase(t):
    # Get data from the test case
    (a, b) = t

    # Evaluate the solution
    solution = a+b
    
    # Returning the solution
    return solution

# Solve 
def solve(input, output):
    # Enumerate all the test cases
    for i, t in enumerate(parse_testcases(input)):
        # Print the solution of the test case
        print(f"Case #{i+1}:", solve_testcase(t), file=output)

current_dir = dirname(__file__)

if __name__ == "__main__":
    # fin = sys.stdin
    # fout = sys.stdout
    # If you want to read and write from files use these two lines:
    fin = open(join(current_dir, "./input.txt"), "r")
    fout = open(join(current_dir, "./output.txt"), "w")
    print("Read")
    solve(fin, fout)
