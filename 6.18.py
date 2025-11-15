# read coordinates from keyboard
x = float(input('Enter x coordinate: '))
y = float(input('Enter y coordinate: '))
print(f"x = {x}")
print(f"y = {y}")
if x == 0 and y == 0:
    pos = 'origin'
elif x == 0:
    pos = 'y-axis'
elif y == 0:
    pos = 'x-axis'
elif x > 0 and y > 0:
    pos = 'first quadrant'
elif x < 0 and y > 0:
    pos = 'second quadrant'
elif x < 0 and y < 0:
    pos = 'third quadrant'
else:
    pos = 'fourth quadrant'
print(f"Point P({x},{y}) is in the {pos} of the coordinate system")
