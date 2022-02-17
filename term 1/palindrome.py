str=input("Enter the string: ")
l=len(str)
p=1-1
index=0
while (index<p):
    if(str[index]==str[p]):
        index=index+1
        p=p-1
    else:
        print("String is not a palindrome")
        break
else:
    print("String is a palindrome")
