sum = 0
str1 = ''
file = open("latex.log", 'r')
counts = {}
for line in file.readlines():
    for ch in line:
        counts[ch] = counts.get(ch, 0) + 1
file.close()
for item in counts:
    sum = sum + counts.get(item)
for i in range(26):
    if counts.get(chr(ord('a')+i)):
        str1 = str1 + chr(ord('a')+i) + ':' + str(counts.get(chr(ord('a')+i)))
    if i != 25:
        str1 = str1 + ','
print("共{0:}字符,{1:}".format(sum,str1))