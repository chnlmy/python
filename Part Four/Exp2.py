import random
random.seed(123)
N = eval(input())
hits = 0
i = 0
for i in range(N):
    x = random.random()
    y = random.random()
    dist = pow((x**2 + y**2), 0.5)
    if dist <= 1:
        hits = hits + 1
pi = 4 * (hits / N)
print("{:.6f}".format(pi))