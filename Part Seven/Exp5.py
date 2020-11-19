file = open("/Users/liumingyi/github/python/Part Seven/data.csv","r")
for line in file:
    line = line.replace(" ","")
    print(line, end='')