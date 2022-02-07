d1=dict()
i=1
n=int(input("Enter the number of Entries: "))
while i<=n:
    c=input("Enter country: ")
    cap=input("Enter capital: ")
    cur=input("Enter currency of country: ")
    d1[c]=(cap,cur)
    i=i+1
l=d1.keys()
print(f'\n Country \t\t Capital \t\t Currency')
for i in l:
    z=d1[i]
    print(f'\n {i}\t\t',end="\t\t")
    for j in z:
        print(f'{j} \t\t',end="")
    #searching
x=input(f'\nEnter country to be searched: ')
for i in l:
    if i==x:
        print(f'\nCountry\t\t Capital\t\t Currency\t\t')
        z=d1[i]
        print(f'\n{i}\t\t', end="")
        for j in z:
            print(f'{j}\t\t',end="\t\t")
        break