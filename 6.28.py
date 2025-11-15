n = int(input('Enter how many Fibonacci numbers to print (e.g. 20): '))
a, b = 0, 1
for idx in range(n):
    # print each Fibonacci term as it's generated
    if idx < n - 1:
        print(a, end=' ')
    else:
        print(a)
    a, b = b, a + b
