import time
wid = 50
print("执行开始".center(wid//2, '-'))
start = time.perf_counter()
for i in range(101):
    str1 = '*' * i
    str2 = '-' * (100-i)
    t = time.perf_counter() - start
    print("\r{:>3.0f}%[{}->{}]{:.2f}s".format(i, str1, str2, t), end='')
    time.sleep(0.05)
print("\n"+"执行结束".center(wid//2, '-'))