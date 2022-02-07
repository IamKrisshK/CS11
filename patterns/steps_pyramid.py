x=int(input("Enter value of x: "))
n= 1
for j in range(1,x+1):
    for k in range (x,0,-1):
        if k>j:
            print(' ', end = '')
        else:
            print(n, end = ' ')
            n+=1
    print()

#  1 
# 2 3 
#4 5 6 