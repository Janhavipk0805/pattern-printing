n=5 # we want 5 rows
for i in range(1,n+1): # repeat pattern 5 times
    for j in range(n-i): # print spaces before stars
        print(" ",end = " ")
    for j in range(i):
     print("*",end =" ")
    print()