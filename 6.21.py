amount = int(input('Enter the amount in PLN: '))
coins5 = amount // 5
amount2 = amount - coins5 * 5
coins2 = amount2 // 2
coins1 = amount2 - coins2 * 2
print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {coins5}")
print(f"2 PLN coins: {coins2}")
print(f"1 PLN coins: {coins1}")
