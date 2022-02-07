list=[1,3,5,7,8]
final_list=[list[0]]
for i in range(1,len(list)):
    final_list += [final_list[i-1]+list[i]]
print(final_list)