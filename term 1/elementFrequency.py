L=[3,21,5,6,3,8,21,6]
L1=[]
L2=[]
for i in L:
    if i not in L2:
        x=L.count(i)
        L1.append(x)
        L2.append(i)
print(f'Element \t\t frequency')
for i in range(len(L1)):
    print(f'{L2[i]}\t\t\t{L1[i]}')
