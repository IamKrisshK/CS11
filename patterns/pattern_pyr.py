x=int(input("Enter value of x: "))
for j in range(1,x+1):
    n = 1
    for k in range(x,0,-1):
        if k>j:
            print (end = ' ')
        else:
            for l in range (n,0,-1):
                print (l, end = '')
                l+=1
                if n == 1:
                    break
            n+=1
    print()

#  1
# 121
#121321