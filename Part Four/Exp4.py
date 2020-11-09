b = 0
for i in range(100,999):
    x = int(i / 100)
    y = int(i / 10  % 10)
    m = int(i % 10)
    if i == (x**3 + y**3 + m**3):
        if b != 0:
            print(',',end='')
        print("{}".format(i), end='')
        b = b + 1
    i = i + 1