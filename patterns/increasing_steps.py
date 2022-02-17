x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))
v = 1
for i in range(x):
    for m in range(1,y):
        print(v,end = ' ')
        v+=1
    y+=2
    print("")

# x=3 y=3
#1 2 
#3 4 5 6 
#7 8 9 10 11 12 