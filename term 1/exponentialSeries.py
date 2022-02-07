x = float(input("Enter  value of x: "))
n = int(input("Enter limit: "))
s = 1
total =1
for i in range(1,n+1):
    s = s*i
    total=total+((x**i)/s)
print(f'Exponential series for x ={x} and n={n} is {total}')