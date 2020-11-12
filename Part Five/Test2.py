def prime(m):
    global i
    while i < 5:
        for j in range(2,m):
            if m % j == 0:
                break
        else:
            i = i + 1
            if i < 5:
                print(m,end=',')
            else:
                print(m)
        prime(m+1)
i = 0
n = eval(input())
prime(round(n))