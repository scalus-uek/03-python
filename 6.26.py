correct_pin = '0805'
max_attempts = 3
for attempt in range(1, max_attempts + 1):
    a = input('Enter the PIN code: ')
    if a == correct_pin:
        print('Correct!')
        break
    else:
        print('Incorrect...')
else:
    print('Sorry, your payment card has been blocked.')
