
age = int(input("Enter your age: "))

if age < 13:
    group = "Child"
elif age <= 19:
    group = "Teen"
elif age <= 64:
    group = "Adult"
else:
    group = "Senior"

print(f"You are a {group}.")