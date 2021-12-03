## Day 3 puzzles

import sys

# Create input with test values as default
inputs = [
    '00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100',
    '10000', '11001', '00010', '01010'
]

# TODO Read in file input here

# ---- Problem 1 solution ----

# Loop through and find most common state for each bit
result = []

# Loop through each input
for input in inputs:
    # Loop through each bit in order and increment occurence of it
    for bit in range(len(input)):
        print("todo")
