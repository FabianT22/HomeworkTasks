for i in range(100, 0, -1):
    if i % 3 == 0 and i % 5 == 0:
        print(f'Testing {i}')
    elif i % 5 == 0:
        print(f'Agile {i}')
    elif i % 3 == 0:
        print(f'Software {i}')
    else:
        print(i)
