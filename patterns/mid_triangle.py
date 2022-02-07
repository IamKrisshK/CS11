x=int(input("Enter value of x: "))
#for the upper triangle
#loop for rows
for i in range (0,x):
    #loop for numbers
    for j in range(1,i+1):
        print (j, end = ' ')
    print()
#for the lower triangle
#for the number of rows
for i in range (x, 0, -1):
    #for the numbers
    for j in range(1,i+1):
        print (j, end = ' ')
    print()

#1 
#1 2 
#1 2 3 
#1 2 
#1