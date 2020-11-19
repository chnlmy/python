dic = {}
sum = 0
file = open("/Users/liumingyi/github/python/Part Seven/latex.log", 'r')
for line in file.readlines():
    dic[line] = dic.get(line, 0) + 1
for i in dic:
    if dic.get(i) == 1:
        sum = sum + 1
print("共{:}独特行".format(sum))