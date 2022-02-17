x=int(input("Enter value for x: "))
#loop for rows
for i in range(x,0,1):
    #for numbers
    for j in range (1,i+1):
        print (j, end = ' ')
    print (' ')
    i+=1