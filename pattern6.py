n=5 # we want 5 rows
for i in range(1,n+1): # repeat pattern 5 times
    for j in range(n-i): # print spaces before stars
        print(" ",end = " ")
<<<<<<< HEAD
    for j in range(i): # print stars in each row
     print("*",end =" ")
    print() # move to next line
=======
    for j in range(i): # print stars(1 star in first row, 2 in second,etc.)
     print("*",end =" ")
    print() # go to next row
>>>>>>> 1b9d02cba708d4d3576b86acab85a3b182889882
