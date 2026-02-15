import random
numbers=[]
for i in range(20):
    num=random.randrange(1,100)
    numbers.append(num)
print("List of the numbers: ",numbers)
#average
total=0
for num in numbers:
    total=total+num
    average=total/20
print("Average: ",average)
# largest,smallest
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
if num<smallest:
        smallest=num
print("Largest: ",largest)
print("Smallest: ",smallest)
# increasing order
for i in range(19):
    for j in range(19-i):
        if numbers[j]>numbers[j+1]:
            temp=numbers[j]
            numbers[j]=numbers[j+1]
            numbers[j+1]=temp
print(numbers)
#ss,ls
ss=numbers[1]
ls=numbers[-2]
print("Second smallest:",ss)
print("Second largest: ",ls)
#even count
count=0
for num in numbers:
    if num%2==0:
        count+=1
print("Even count: ",count)
    
            
