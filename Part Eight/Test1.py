str1 = input()
for ch in str1:
    if ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z'):
        print(ch, end = '')
    else:
        continue