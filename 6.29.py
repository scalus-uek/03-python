N = int(input('Enter how many prime numbers to find (N): '))
found = 0
candidate = 2
while found < N:
    is_prime = True
    if candidate < 2:
        is_prime = False
    elif candidate == 2:
        is_prime = True
    elif candidate % 2 == 0:
        is_prime = False
    else:
        i = 3
        while i * i <= candidate:
            if candidate % i == 0:
                is_prime = False
                break
            i += 2
    if is_prime:
        # print prime immediately; print newline after last one
        if found < N - 1:
            print(candidate, end=' ')
        else:
            print(candidate)
        found += 1
    candidate += 1
import sys
sys.stdout.write("\n")
