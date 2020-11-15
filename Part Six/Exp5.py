import jieba
txt = open("/Users/liumingyi/github/python/Part Six/沉默的羔羊.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) <= 2:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
word, count = items[0]
print(word)
