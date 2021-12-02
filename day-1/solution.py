import sys
import functools

# Problem 1: Using the input file, compare each value to its previous value
# to see if there was an increase in the depth. If there was an increase from
# the previous value, record it. The solution to the first problem is to count
# the number of times that the depth increased. Answer was `1195`

def number_of_increases(list):
    """
    Iterates through the list and counts how many times the current item is greater
    than the previous item. Skips first index as you cannot compare it to a nil index.
    Returns the count of increases

    Example: 
    list = [1, 2, 3, 5, 4] 
    print(number_of_increases(list)) # prints 3
    """
    count = 0
    for i in range(1, len(list)):
        if list[i] > list[i - 1]:
            count += 1
    return count

# Store input in array
lines = []

# Read in the lines from the input file and convert to ints
file = open(sys.argv[1], "r") 
for line in file.readlines():
    lines.append(int(line))

print("Num of increases: ", number_of_increases(lines))

# Problem 2: Too much noise this way. Start at the first number, count by
# threes and sum the three numbers. Create a new list with the sums, then
# count how many times there have been increases.

# Calculate the sums and store in `sums`
sums = []

for i in range(len(lines)):
    # Slice the subset of numbers we want to sum and calculate the sum using reduce
    list = lines[i: i + 3]
    sum = functools.reduce(lambda a,b: a + b, list)

    # Add the sum to the new list of sums
    sums.append(sum)

print("Num of increases by threes: ", number_of_increases(sums))
