
# What is wrong with this?
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
# The above will add 'O' 'k' 'e' as new separate items in the list.
# So should be written as below with [] brackets.
cheese += ['Oke']
# To add two new cheeses with a single command you would do the following.
cheese.extend(['Brie', 'Nacho'])
print(cheese)


