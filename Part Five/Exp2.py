def cmul(*b):
    s = 1
    for item in b:
        s = s *item
    return s
print(eval("cmul({})".format(input())))