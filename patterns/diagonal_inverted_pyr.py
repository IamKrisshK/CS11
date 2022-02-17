x=int(input("Enter value of x: "))
for j in range(x,0,-1):
    k = 1
    for l in range(0,j+1):
        if j>l:
            print (end = ' ')
        else:
            for k in range(1,l):
                print(' ', k, end = '')
            k+=1
    print()

#Enter value of x: 5
#       1  2  3  4
#      1  2  3
#     1  2
#    1