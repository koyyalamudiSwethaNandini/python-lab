String1=input("Enter String1:")
String2=input("Enter String2:")
if len(String1)==len(String2):
    print("Strings with same length")
    for i in range(len(String1)):
        print(String1[i],end=" ")
        print(String2[i],end=" ")
else:
    print("Strings with different lengths")


