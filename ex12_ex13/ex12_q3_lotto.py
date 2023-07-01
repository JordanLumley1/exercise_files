# Write a python script that will generate and display six unique random
# lottery numbers between 1 and 50. Think about  which python data
# structure is best suited to store the numbers. Use the python help()
# function to find out which function to use from the python standard
# library called RANDOM.

import random

# Calling help function.
# help()

# Assign random.sample to the lucky_dip variable, ask it to choose a random number
# with the range of 1-50, six times.
# random.sample(range(start, end), amount of times).

lucky_dip = random.sample(range(1, 50), 6)
print(lucky_dip)

