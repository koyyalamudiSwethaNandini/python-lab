f = open(r'C:\Users\koyya\OneDrive\Desktop\swetha\14\Sample.txt', 'r')

for x in f:
    print(x.strip(), end=";")

f.close()
