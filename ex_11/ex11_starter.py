#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,' \
          'Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)

print('')
print('')

# Task 3a
# Finds length of belgium and prints a hyphen for every character in the string.
belgium_length = len(Belgium)
print('-'*belgium_length)

print('')
print('')

# Replaces all instances of the first with the second.
# Can this be changed to replace all alpha and numerical?
print(Belgium.replace('o', '-'))

print('')
print('')

# Task 3b
# Replace all commas with a colon.
print(Belgium.replace(',', ':'))

print('')
print('')

# Task 3c
# Find the index values of the numbers we are looking for.
# Add the population of Belgium and Brussels together.
# Populations must be changed from a string to an integer.

Belgium_population = int(Belgium[8:16])
Brussels_population = int(Belgium[26:32])
combined_population = (Belgium_population + Brussels_population)
print(combined_population)
