#Q.10 Hollow Square Pattern
n = 5 # total no. of rows and columns
for i in range(n): # Print 5 rows
    for j in range(n): # Print 5 columns
        if i == 0 or i ==n-1 or j== 0 or j==n-1: # print stars on border of square
            print("*",end = " ")
        else: # print spaces in square
            print(" ",end = " ")
    print() # move to the next row