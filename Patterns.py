def dgr(x):
    #for the number of rows
    for i in range(1,x+1):
        #for the numbers
        for j in range(1,i+1):
            print(j, end = ' ')
        print(end = '\n')

def _dgr(x):
    for num in range (x+1):
        for i in range (num):
            print(num, end = ' ')
        print (' ')

def inv(x):
    for  i in range(x,0,-1):
        for j in range (1,i+1):
            print (j, end = ' ')
        print (' ')

def _inv(x):
    #loop for rows
    for i in range(x,0,-1):
        #for numbers
        for j in range (1,i+1):
            print (j, end = ' ')
        print (' ')
        i-=1

def tri(x):
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

def di_inv(x):
    #for the inverse number printed patterns
    #for the rows
    for i in range(0,x):
        #for the number of rows
        for j in range (i+1,0,-1):
            print (j, end = ' ')
        print()

def stp(x, y):
    v = 1
    for i in range(x):
        for m in range(1,y):
            print(v,end = ' ')
            v+=1
        y+=2
        print("")

def rat(x):
    for v in range(1,x+1):
        i = 1
        for j in range (x,0,-1):
            if j>v:
                print(' ', end = ' ')
            else:
                print(i, end = ' ')
                i+=1
        print()
        
def pyramid(x):
    n= 1
    for j in range(1,x+1):
        for k in range (x,0,-1):
            if k>j:
                print(' ', end = '')
            else:
                print(n, end = ' ')
                n+=1
        print()
def pyr_(x):
    for j in range(1,x+1):
        n = 1
        for k in range(x,0,-1):
            if k>j:
                print(end = ' ')
            else:
                print(n, end = ' ')
                n+=1
        print()

def rck_pyr(x):
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

def pyr(x):
    for j in range (0,x+1):
        n = 1
        for k in range (x,0,-1):
            if k>j:
                print(end = ' ')
            else:
                print(n, end = '')
                n+=1
        print()
def inv_pyr(x):
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
