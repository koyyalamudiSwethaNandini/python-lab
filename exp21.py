from itertools import permutations
s=input("Enter a word")
for i in range(2,len(s)): 
    for p in permutations(s,i):
            print(' '.join(p),) 
