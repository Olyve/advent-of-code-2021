# Day 2 - Read the input file where each line is in the format of
# `<direction> <distance>` to figure out where the sub will move,
# starting from 0,0

import sys

# Store file input
input = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8),
         ("forward", 2)]

# If a file path was provided use it, otherwise use default test data
if len(sys.argv) > 1:
    # Read in the input file line by line and convert to list of tuples
    file = open(sys.argv[1], "r")
    input = []  # Reset input
    for line in file.readlines():
        line = line.split(' ')
        input.append((line[0], int(line[1])))

# Set starting x and y position
x = 0
y = 0

# Loop through input and update position for each instruction
for instruction in input:
    if instruction[0] == "forward":
        x += instruction[1]
    elif instruction[0] == "down":
        y += instruction[1]
    else:
        y -= instruction[1]

print("x: ", x)
print("y: ", y)

product = x * y
print("product: ", product)

## Part 2
x = 0
y = 0
aim = 0

# Loop through input and update position and aim
for command in input:
    if command[0] == "forward":
        x += command[1]
        y += (aim * command[1])
    elif command[0] == "down":
        aim += command[1]
    else:
        aim -= command[1]

print("Part 2")
print(x)
print(y)
print(x * y)
