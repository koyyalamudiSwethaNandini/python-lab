def root(X,n=2):
    return X**(1/n)
X=int(input("Enter a number:"))
n=int(input("Enter a number:"))
res1=root(X,n)
res2=root(X)
print("The value without default n=",res1)
print("The value with default n=",res2)


