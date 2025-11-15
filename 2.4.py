###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.
#
number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if(number2 == 0):
        print('Error: Division by zero')
        result = None
        exit()
    else:
        result = number1 / number2
else:
    result = None
    print('Incorrect operator entered')
# print result
if result is not None:
    print(f'{number1} {operator} {number2} = {result}')