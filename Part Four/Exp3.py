i = 1
sum = 0
for i in range(1, 967):
    j = pow(-1, i+1) * i
    sum = sum + j
print(sum)