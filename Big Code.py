#Code 1 - Code for product
def product(q,r):
    pro = q*r
    return pro

#Code2 - Code for Calc SI
def simpin(p,r,t):
    si = p*(r/100)*t
    return si

#Code3 - Odd-Even number checker
def oddeve(x):
    if x%2 == 0:
        return (x, ' is even')
    elif x%2 != 0:
        return (x, ' is odd')
    else:
        return ('error')

#Code4 - Grade finder
def grd(l):
    if l in range (91,101) == True:
        return 'A+'
    elif l in range (81,91) == True:
        return 'A'
    elif l in range (71,81) == True:
        return 'B+'
    elif l in range (61,71) == True:
        return 'B'
    elif l in range (51,61) == True:
        return 'C+'
    elif l in range (41,51) == True:
        return 'C'
    elif l in range (31,41) == True:
        return 'D'
    elif l in range (0,31) == True:
        return 'Fail'
    else:
        return('error')

#Code5 - Fibonacci Series upto a certain limit
def fib(u):
    n1 = 0
    n2 = 1
    n3 = 1
    while (n3<=u):
        print (n3, end = ' ')
        n1=n2
        n2=n3
        n3=n1+n2

#Code6 - Prime Numbers upto a certain limit
def prime_printer(k,l):
    for i in range(l, k+1):
        o = 2
        while o<i:
            if i%i == 0:
                break
            o = o+1
        else:
            print(i, ' is a Prime Dragon!!')

#Code7 - Armstrong number checker
def is_armstrong(u):
    m = len(u)
    sum = 0
    v = u
    while v>0:
        a = v%10
        v = int(v/10)
        sum += (u**m)
    if sum == u:
        return "Yes it is!"
    else:
        return "No it isn't!"

#Code8 - Perfect number checker
def is_perf(k):
    po = 0
    for i in range(1,k):
        if k%i == 0:
            po+=i
        i = i+1
    if po == k:
        return "Yes it is!"
    else:
        return "No it isn't!"

#Code9 - Sum of factorial series
def factorials(x):
    l = 1
    for c in range (0,x):
        if c == 0 or c==1:
            l = 1        
        elif x%c == 0:
            l*=c
        c+=1
    return c

def fact_series(x,n):
    o = 1
    for v in range(1,n+1):
        print(o, end = '\n')
        print((x**v)/factorials(x), end = '\n')
        v = v+1

def sum_fact_series(x,n):
    o = 0
    for v in range(0,n+1):
        o += ((x**v)/factorials(x))
        v = v+1
        if x == 1 or x == 0:
            o =float(1)
    return o

def alt_fact_sum(x,n):
    o = 1
    for v in range(0,n+1):
        if v == 0 and v%2 == 0:
            o -= ((x**v)/factorials(x))
        else:
            o += ((x**v)/factorials(x))
        v = v+1
    return o

#10.WAP to print the following pattern:11 21 2 3
def ptrn_prnt(x,y):
    i = 0
    while i in range(0,y+1):
        print (x*i, end = '\n')
        i = i+1

def quan_ana(c,v,m):
    #molarity of naoh c
    #volume of naoh v
    #volume of hcl m
    x =((c*v)/m)
    stren = x*36.460
    print (stren)
    return x

#Code15 - The second largest element of a list
def sec_high(x):
    x = list(x)
    n = max(x)
    secmax = x[0]
    for i in range (1, len(x)):
        if x[i]>secmax and x[i]<n:
            secmax=x[i]
    return secmax

def number_receiver(x):
    i = 0
    l = []
    while i in range(0,x):
        x = int(input('Enter the number: '))
        print((x), end = '\n')
        l.append(int(x))
        i = i+1
    l = l.sort
    min = l[0]
    max = l[-1]
    avg = (l.sum)/len(l)

    return 'Max value is: '+ max, '\n', 'Min value is: ' +min, '\n', 'Avg is: ' +avg

#Code11 - WAP to accept a string and display whether it is a palindrome
def palin_chk(x):
    x = list(x)
    u = 0
    l = -(u+1)
    if x[u] == x[l]:
        return True
    else:
        return False

#Code12 - Character Counter.
def chr_counter(x):
    alph = 0
    dig = 0
    upp_alph = 0
    low_alph = 0
    wht_spc = 0
    other = 0
    ttl_chr = len(x)
    for i in x:
        if i.isalpha() ==  True:
            alph += 1
            if i.isupper() == True:
                upp_alph += 1
            else:
                low_alph += 1
        if i.isdigit() == True:
            dig += 1
        if i.isalnum() != True:
            wht_spc += 1
    other = ttl_chr - (alph + dig + wht_spc)
    return 'Total Characters: %s \n Alphabets: %s \n \t UpperCase: %s \n \t Lowercase: %s \n Numerals: %s \n White Characters: %s \n Other Characters: %s' %(ttl_chr, alph, upp_alph, low_alph, dig, wht_spc, other)

#Code13 - Word Capitalizer
def sen_caps(x):
    return x.title()

#Code14 - Odd one out
def odd_1ot (x):
    for i in range(len(x)):
        if i%2 != 0:
            x.pop(x[i])
        else:
            continue
        i += 1
    return x

#Code15 - Pattern
def ptrn(x,y):
    for i in range (0,y+1):
        print(x*i , end = " \n ")
        i+=1
def lst_appndr(x):
        l = []
        for j in range(0,x+1):
            l.append(j)
            j+=1
        return l 
def ptrn_no(x):
    m = lst_appndr(x)
    for j in range(0,x+1):
        for u in m:
            while m.index(u)<= m.index(j):
                print(u, end = '\n')
                if u == j:
                    break
                else:
                    u+=1
    print()

#Code16 - List Cum Display
def lst_cum(x):
    for i in x:
        print(i, end = '\n')
        i=i+1

#Code17 - Element frequencies
def ele_freq(x):
    d = []
    l = 0
    for i in x:
        while i in d == True:
            l = 1
            l += 1
            return i, l
        if i not in d == True:
            l = 1
            d.append(i)
            return i, l
        i += 1

#Code18 - Sort strings with 'A' from a list

def c_sorter(m,p):
    l = []
    for b in p:
        if m not in list(b):
            l.append(b) 
    return l


#Code19 - Sum of all the elements ending with '3'


#Code20 - Shift Postive to right, Negative to left


#Code21 - To swap elements with the next element divisible by 7
def ele_org(x):
    t = []
    for l in x:
        if l in t == False:
            t.append(l)
            for v in range(0,len(t)):
                if l<t[v]:
                    t.insert(v-1,l)
                elif l>t[v]:
                    t.insert(v+1,l)
                v+=1
    return t

#Code22 - Tuple creator
def t_c(c):
    c == str
    c = tuple(c)
    return c

#Code23 - Class record table


#Code24 - Country Capital & Currency data manager
print(ele_org([-1,3,-4,-5,6,3,2,1]))