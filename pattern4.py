#Q.4  Increasing number triangle
n = 5 # Step 1 : Store number of rows and columns
for i in range(1,n+1): #Step 2 : Outer loop control rows
    for j in range(1,i+1): # Step 3: Inner loop prints from 1 to i
        print(j,end = " ") # Step 4: Print number on same line
    print() # Step 5: Move to next row