str1=input("Enter a string: ")

print(f"original string: {str1}")
str2=""
x=str1.split()
for a in x:
    str2 += a.capitalize()+" "
print(str2)