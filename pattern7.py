#Q.7 Star Pyramid Pattern
n = 5 # Total number of rows
for i in range(1,n+1): # This loop prints five rows
    for j in range(n-i): # prints spaces to move star towards the centre
        print(" ",end = " ")
    for j in range(2*i-1): # prints stars in pyramid shape
        print("*",end =" ")

    print() # Move to the next row