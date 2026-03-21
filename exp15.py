def sum_digits(num):
    s = 0
    while num != 0:
        r = num % 10
        s = s + r
        num = num // 10
    return s

n = int(input("Enter a value: "))
r = sum_digits(n)
print("Sum of digits =", r)
