str1 = input()
N = len(str1)
for i in range(N):
    if ord('a') <= ord(str1[i]) <= ord('z'):
        print(chr(ord('a')+(((ord(str1[i])-ord('a')) + 3) % 26)), end='')
    elif ord('A') <= ord(str1[i]) <= ord('Z'):
        print(chr(ord('A')+(((ord(str1[i])-ord('A')) + 3) % 26)), end='')
    else:
        print(str1[i],end='')