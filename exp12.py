s=input("Enter a string:")
str_split=s.split(' ')
str_join='-'.join(str_split)
str_dec={index:ele for index,ele in enumerate(str_split)}
print("Dictionary after splitting")
print(str_dec)
print("string after join with '-'")
print(str_join)
