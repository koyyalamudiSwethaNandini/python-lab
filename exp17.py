def number_of_factors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=" ")
    return
n=int(input("Enter a value to print its factors:"))
print("The factors for given numbers are:")
number_of_factors(n)
