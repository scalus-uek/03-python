n = int(input('Number of products purchased: '))
price = float(input('Product price: '))

# items beyond two get 25% discount
if n <= 2:
    total = n * price
else:
    total = 2 * price + (n - 2) * price * 0.75

print(f"Amount to pay: {total:.2f}")
