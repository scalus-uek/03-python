age = float(input("Enter your dog's age in human years: "))
dog_age = 0

for i in range(1, int(age) + 1):
    if i < 3:
        dog_age += 10.5
    else:
        dog_age += 4

print(f"Your dog's age in dog years is: {int(dog_age)} years")