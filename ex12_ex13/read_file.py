
# Use open and read methods to slurp the entire contents of your pelican.txt file.
# Then print contents of returned data.
with open('pelican.txt', 'r') as infile:
    for line in infile:
        print(line, end="")

print('')
print('')

# Display type of returned data.
print(type('pelican.txt'))

print('')
print('')

# Read pelican.txt file into a list and output number of items in that list.
# Open file and place into variable.
file_open = open('pelican.txt', 'r')

# Read file contents now stored in variable.
read = file_open.read()

# Sort contents of variable into a list, separated by the \n line breaks.
# Then print length of that list.
sort_into_list = read.split('\n')
print(sort_into_list)
print(len(sort_into_list))

print('')
print('')

# loop through list in pelican.txt file and print contents.
open_pelican = open('pelican.txt', 'r')
pelican_list = open_pelican.readlines()
for i in pelican_list:
    print(i)
