# Q.11 Hollow Right-angled triangle
n = 5 # total no. of rows
for i in range(1,n+1): #print 5 rows
    for j in range(1,i+1): # print stars and spaces in each row
        if j==1 or j==i or i==n: # print stars on border of triangle
            print("*",end = " ")
        else: # print spaces inside triangle
            print(" ",end = " ")
    print() # move to the next row