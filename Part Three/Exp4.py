i = 1
N = eval(input())
while 2*i-1 <= N:
    str1 = '*' * (2*i-1)
    print(str1.center(N, ' '))
    i = i + 1