import os

# Complete the function to read the contents of the specified file and print 
# the contents

def printFileContents(filename):
# Student code goes here
 
# expected output: Hello
with open("test.txt", 'w') as f: 
    f.write("Hello")
printFileContents("test.txt")