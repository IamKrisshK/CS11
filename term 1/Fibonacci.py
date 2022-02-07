i = int(input("Enter the limit: "))
x = 0
y = 1
z = 1
print(f'Fibonacci series till {i}')
print(x,y,end = ' ')
while(z <= i):
    print (z, end= " ")
    x = y
    y = z
    z = x+y
