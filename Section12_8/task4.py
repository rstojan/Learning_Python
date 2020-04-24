import os

# Complete the function to create the specified file and return the file name
def createFile(filename):
# Student code goes here
 
# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))