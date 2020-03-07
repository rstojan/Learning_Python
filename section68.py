num_rows = 8
num_cols = 20

rows = 1                       #create a number to start counting from for rows
while rows <= num_rows:        #start iterating through number of rows
    cols = 1                   #create a number to start counting from for columns
    alpha = 'A'                #starting point for alphabet
    while cols <= num_cols:                    #iterates through number of columns
        print('%s%s' % (rows, alpha), end=' ')
        cols +=1                               #number of columns needs to increase
        alpha = chr(ord(alpha) + 1)            #alphabet needs to increase
    rows += 1                                  #number of rows needs to increase
print()   
