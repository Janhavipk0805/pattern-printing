#Q.12 Butterfly Pattern
n = 5 # total no. of rows in upper half
for i in range(1,n+1): # print upper half of butterfly
    for j in range(i): # print stars on half side
        print("*",end = " ")
    for j in range(2 *(n-i)): # print stars in the middle
        print(" ",end = " ")
    for j in range(i): #print stars on the right side
        print("*",end = " ")
    print() # move to the next row

for i in range(n-1,0,-1): # print lower half of butterfly
    for j in range(i): # print stars on left side
        print("*",end = " ")
    for j in range(2*(n-i)): # print stars in the middle
        print(" ",end=" ")
    for j in range(i): # print stars on the right side
        print("*",end = " ")
    print() # move to the next row