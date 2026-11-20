# Q.9 Diamond Star Pattern
n = 5 # Total rows in upper half
for i in range(1,n+1): #print upper half of diamond
    for j in range(n-i): # print space for stars
        print(" ",end = " ")
    for j in range(2*i-1): # print stars in increasing order
        print("*",end = " ")
    print() # move to next row

for i in range(n-1,0,-1): # print lower half of diamond
    for j in range(n-i): # print spaces before stars
        print(" ",end = " ")
    for j in range(2*i-1): # print stars in decreasing order
        print("*",end = " ")
    print() # move to the next row