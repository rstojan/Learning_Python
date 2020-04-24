import os

# Complete the function to append the given new data to the specified file 
# then print the contents of the file

def appendAndPrint(filename, newData):
# Student code goes here
 
# expected output: Hello World
with open("test.txt", 'w') as f: 
    f.write("Hello ")
appendAndPrint("test.txt", "World")