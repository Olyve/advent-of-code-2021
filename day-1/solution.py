import sys

# Track number of increases
num_of_increases = 0

# Store input in array
lines = []

# Read in the lines from the input file and convert to ints
file = open(sys.argv[1], "r") 
for line in file.readlines():
    lines.append(int(line))

# Loop through the inputs and do comparisons for increases
# Hint: Skip first index cause we can't compare to a previous nil value
for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
        num_of_increases += 1

print(num_of_increases)
