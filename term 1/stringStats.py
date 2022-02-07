strl = input("Enter a string: ")
n=c=d=s=u=i=o=0
for ch in strl:
    if ch.isalnum():
        n+=1
        if ch.isupper():
            u=u+1
        elif ch.islower():
            i=i+1
        elif ch.isalpha():
            c=c+1
    if ch.isdigit():
        d=d+1
    elif ch.isspace():
        s=s+1
    else:
        o=o+1

print(f'no of alphabets and digits {n}')
print(f'no of capital alphabets {u}')
print(f'no of small alphabets {i}')
print(f'no of digits {d}')
print(f'no of spaces {s}')
print(f'no of other characters {o}')
