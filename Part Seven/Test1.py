linenum = 0
sum = 0
file = open("/Users/liumingyi/github/python/Part Seven/latex.log", 'r')
for line in file.readlines():
    if len(line) == 1:
        continue
    else:
        sum = sum + len(line) - 1
        linenum = linenum + 1
ava = sum / linenum
print(round(ava))