sum = 0
for i in range (2,100):
    n = 0
    for j in range(2,i):
        if i%j == 0:
            n = 1
    if n == 0:
        sum = sum + i
print(sum)