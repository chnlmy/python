import random

def genpwd(length):
    pwd = 0
    for i in range(length):
        pwd = pwd * 10 +random.randint(0,9)
    return pwd

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))