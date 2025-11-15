###
# Sums numbers entered by user
#
total_sum = 0
idx = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    idx += 1

mean = total_sum  / idx
print(f"The mean of the numbers is: {mean}")