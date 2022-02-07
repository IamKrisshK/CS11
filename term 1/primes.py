x = int(input("Enter limit: "))
for num in range(x+1):
    i = 2
    while i<num:
        if num%i ==0:
            break
        i = i+1
    else:
        print(f'{num} is a prime number.')