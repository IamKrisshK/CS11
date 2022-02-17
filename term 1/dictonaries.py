classxi=dict()
n=int(input("Enter total number of sections in 11th class: "))
i=1
while i<=n:
    a=input("Enter Section: ")
    b=input("Enter stream name: ")
    classxi[a]=b
    i=i+1
print(f'Class \t Section \t Stream name')
for i in classxi:
    print(f'XI \t {i} \t {classxi[i]}')
