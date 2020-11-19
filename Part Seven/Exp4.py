file = open("/Users/liumingyi/github/python/Part Seven/data.csv",'r')
ls = []
for line in file:
    line = line.replace("\n", '')
    ls.append(line.split(","))
for rol in ls:
       rol = rol[::-1]
       for i in range(len(rol)):
           if i == len(rol) - 1:
               print(rol[i], end = '\n')
           else:
               print(rol[i], end = ',')
file.close()