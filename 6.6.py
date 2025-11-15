hours = int(input("Enter the number of hours: "))

if hours > 6:
    print("The fee is 20 PLN")
elif 3 <= hours <= 6:
    print("The fee is 15 PLN")
elif 1 <= hours < 3:
    print("The fee is 5 PLN")
else:
    print("Wrong input")