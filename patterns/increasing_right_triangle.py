x=int(input("Enter value of x: "))
for v in range(1,x+1):
    i = 1
    for j in range (x,0,-1):
        if j>v:
            print(' ', end = ' ')
        else:
            print(i, end = ' ')
            i+=1
    print()

#        1 
#      1 2 
#    1 2 3 
#  1 2 3 4 
#1 2 3 4 5 