x=int(input("Enter value of x: "))
#for the inverse number printed patterns
#for the rows
for i in range(0,x):
    #for the number of rows
    for j in range (i+1,0,-1):
        print (j, end = ' ')
    print()

#1 
#2 1 
#3 2 1 
#4 3 2 1 
#5 4 3 2 1