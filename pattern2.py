# Q.2 Right-angled triangle pattern
n=5 # Step 1 : Store no. of rows
for i in range(n): # Step 2: Outer loop control rows
    for j in range(i+1): #Step 3 : inner loop print star in each row
                         # i+1 means each row gets one extra star 
        print("*",end = " ") # Step 4 : Print star on the same line

    print() # Step 5: Move to next row