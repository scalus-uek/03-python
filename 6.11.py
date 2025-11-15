current_price = 140.00
previous_price = 200.00

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

if previous_price == 0:
    print("Previous price is zero, cannot compute percentage change.")
else:
    change_percent = (previous_price - current_price) / previous_price * 100
    if current_price < previous_price:
        if change_percent >= 10:
            print("Buy the product!!")
        print(f"Product price reduced by {round(change_percent)}%")
    elif current_price > previous_price:
        print(f"Product price increased by {round(-change_percent)}%")
    else:
        print("Product price unchanged")