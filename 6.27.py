i = 6
while i >= 0:
    for j in range(1, 4):
        if j < 3:
            print(f"{i + j}", end=' ')
        else:
            # last in row prints newline by default
            print(f"{i + j}")
    i -= 3
