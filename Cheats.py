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

def fact(x):
    l = 1
    k = 1
    while x>1:
        l*= x
        x-=1
    return l
def fact_series(x,n):
    o = 1
    k = 0
    while n>0:
        k+= (x/(fact(x)))
        n-=1
    return k
print(fact_series(4,2))

def ele_org(x):
    l = []
    for p in x:
        l.append(p)
    l.sort()
    return l
def _ele_org(x):
    t  = 0
    for i in range (0,len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                t = x[i]
                x[i]= x[j]
                x[j]=t
    return x
print (_ele_org([1,2,3,5,4]))

def ptrn(x):
    for j in range (0,x+1):
        for k in range (j,0,-1):
            print(end = ' ')
        for k in range(1,j):
            print(k, end = ' ')
        print()


def ptrn_(x):
    for k in range (x,0,-1):
        l = 1
        for j in range(1,x+1):
            if j>k:
                print(end = '')
            else:
                print(l, end = ' ')
                l+=1
        print()
def _ptrn_(x):
    for j in range(x,0,-1):
        k = 1
        for l in range(0,j+1):
            if l>j:
                print (end = ' ')
            else:
                print(k, end = ' ')
                k+=1
        print()
print(_ptrn_(5))