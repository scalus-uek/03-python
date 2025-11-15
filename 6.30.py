for row in range(1, 8):
    for col in range(0, 7):
        if col < 6:
            print(row + col * 7, end=' ')
        else:
            print(row + col * 7)
