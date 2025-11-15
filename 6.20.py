n = int(input('Enter decimal number: '))
if n == 0:
    b = '0'
else:
    b = ''
    num = n
    while num > 0:
        # prepend remainder to build binary string without using a list
        b = str(num % 2) + b
        num //= 2
print(f"{n}(10) = {b}(2)")
