import jieba
import os
from collections import Counter
ROOT = os.path.expanduser("~/github/python/03-wordcloud/")
def getPath(dir_path, file_name):
    return os.path.join(dir_path, file_name)
def readContent(path):
    with open(path, mode="r+", encoding="utf-8") as file:
        content = list(map(lambda item: item.strip(),file.readlines()))
    return content
comments = readContent(path = getPath(ROOT, "comments.txt"))
stopwords = readContent(path = getPath(ROOT, "stopwords.txt"))
comments = "".join(comments)
words = []
for word in jieba.lcut(comments):
    if word not in stopwords and word != ' ' and not word.isdigit() and len(word)>=2:
        words.append(word)
wordsCounter = Counter(words)
import matplotlib.pyplot as plt
from matplotlib.image import imread
background_img = imread(getPath(ROOT, 'nezha.jpg'))
from wordcloud import WordCloud, ImageColorGenerator
wc = WordCloud(
    background_color="white",
    mask=background_img,
    scale=20,
    font_path=getPath(ROOT, "Songti.ttc")
)
wc.generate_from_frequencies(wordsCounter)
img_colors = ImageColorGenerator(background_img)
plt.figure(figsize=(13,8))
plt.axis('off')
wc.to_file(getPath(ROOT, "wordcloud.jpg"))