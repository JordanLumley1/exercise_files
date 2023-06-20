import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
# add search criteria before the asterix for file names starting with that letter
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
print(glob.glob(pattern))

print('')

# TODO: use os.path.getsize to find each file's size
fileList = (glob.glob(pattern))
print(fileList)
for x in fileList:
    print(x, os.path.getsize(x))

print('')

# TODO: Add a test to only display files that are not zero length
list = glob.glob(pattern)
for x in list:
    if os.path.getsize(x) > 0:
        print(x, os.path.getsize(x))

print('')

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
list = glob.glob(pattern)
for x in list:
        print(os.path.basename(x), os.path.getsize(x))

print('')
print('')

list = glob.glob(pattern)
for x in list:
    if os.path.getsize(x) > 0:
        print(os.path.basename(x), os.path.getsize(x))
