###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0

idx = 1
# Calculate the sum of even numbers
while idx <= N:
    if idx % 2 == 0:
        sum_even += idx
    idx += 1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")