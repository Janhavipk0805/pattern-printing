# Q.1 Solid Square Pattern
# Step 1 : Store number of rows and columns
n=4
#Step 2: Outer loop is used to print 4 rows
for i in range(n):
    for j in range(n): # Step 3 : inner loop prints 4 stars in each row
        print("*",end = " ") # Step 4 : Print star on same line 
    print() # Step 5 : Move to next line after printing 4 stars