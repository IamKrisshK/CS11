L=[2,-5,6,8,]
length=len(L)
print(f"Original list {L}")
for i in range(length-1):
    for j in range(length-i-1):
        if L[j]<0:
            L[j], L[j+1]=L[j+1],L[j]
print(f"After shifting list is {L}")
