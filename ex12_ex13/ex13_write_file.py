# Write a line of code to create a file handle to open and append to file
# called pelican.txt .

# Creating a .txt file x = open('new file name.txt', 'w')
f = open('pelican.txt', 'w')

# append the following line to the file using the write
# method of the file handle.
output = open('pelican.txt', 'w')
output.write("A wonderful bird is the pelican, ")

# append a second line using write.
output_2 = open('pelican.txt', 'w')
output.write("His bill holds more than his belican.")

# Create a list.
lines = ["\nHe can take in his beak, \n", "Enough food for a week, \n"
         "But I'm damned if I see how the helican.\n"]

# append list to .txt file
output_3 = open('pelican.txt', 'w')
output.writelines(lines)

# The "\n" 's are required for text on a new line.