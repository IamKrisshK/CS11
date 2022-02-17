print("Simple interest calculation:\n")
print("Enter the following details: ")
p = int(input("Amount: "))
r = int(input("Rate of Interest: "))
t = int(input("number of years: "))
s = (p*r*t)/100
print(f'Simple interest is {s}')
