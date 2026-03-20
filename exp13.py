source_list=[1,1,2,3,4,3,0,0]
final_list=[]
for val in source_list:
    if val not in final_list:
        final_list.append(val)
print('Given list of elements:')
print(source_list)
print('List after removing duplicates is')
print(final_list)
