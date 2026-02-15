word=input("Enter a word: ")
vowels='aeiouAEIOU'
flag=0
a=" "
for letter in word:
    if letter in vowels:
        a=letter
        flag=1
        break
if flag ==1:
    print("Word contains vowels: ",a)
else:
    print("Word does not contain vowels")
