#write a program to print 1 12 123 1234
def al(x):
    for i in range (1,x+1):
        for j in range (1, i+1):
            print(j, end = ' ')
        print()

def sh(x):
    x.sort()
    y = len(x)
    y -=1
    return x[-2]

def sel(x,n):
    l = 5-n
    o = []
    for k in x:
        if (k+l)%5 == 0:
            o.append(k)
        else:
            continue
    return sum(o)

