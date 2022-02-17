L=['AUSHIM','LEENA','AKHTAR','HIBA','NISHANT','AMAR']
count =0
for i in L:
    if i[0] in ('aA'):
        count+=1
        print(i)
print(f"Appearing {count} times.")