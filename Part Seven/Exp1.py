linenum = 0
file = open("/Users/liumingyi/github/python/Part Seven/latex.log", 'r')
for line in file.readlines():
    if len(line) == 1:
        continue
    else:
        linenum = linenum + 1
file.close()
print("共{:}行".format(linenum))