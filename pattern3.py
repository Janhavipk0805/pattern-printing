# Q.3 Inverted Right-angled triangle
n = 5 #Step 1: Store no. of rows
for i in range(n): #Step 2: Outer loop controls the rows
    for j in range(n-i): # Step 3: inner loop prints decreasing stars
        print("*",end = " ") # Step 4: Print stars on the same line
    print() # Step 5: Move to next row