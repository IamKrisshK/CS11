L=[-12,11,-13,-5,6,-7,5,-3,-6]
n=len(L)
print("Original List:",L)
for i in range(n-1):
    for j in range(n-i-1):
        if L[j]<0:
            L[j],L[j+1]=L[j+1],L[j]
print("After shifting list is: ",L)