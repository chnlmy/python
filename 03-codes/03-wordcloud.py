#!usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from collections import Counter

import jieba
import matplotlib.pyplot as plt
from matplotlib.image import imread
from wordcloud import ImageColorGenerator, WordCloud

# 定义文件路径
ROOT = os.path.expanduser("~/Desktop/03-wordcloud/")  

# 定义路径拼接函数
def getPath(dir_path, file_name): 
    return os.path.join(dir_path, file_name) 

# 定义读取文件内容函数
def readContent(path): 
    with open(path, mode="r+", encoding="utf-8") as file: 
        content = list(map(lambda item: item.strip() ,file.readlines())) 
    return content 

# 分别读取评论文本和停止词
comments = readContent(path = getPath(ROOT, "comments.txt")) 
stopwords = readContent(path = getPath(ROOT, "stopwords.txt")) 

comments = "".join(comments)


# jieba 分词
words = [] 
for word in jieba.lcut(comments): 
    if word not in stopwords and word != ' ' and not word.isdigit() and len(word)>=2: 
        words.append(word) 

wordsCounter = Counter(words) 

# 词云
background_img = imread(getPath(ROOT, 'nezha.jpg'))


#1. 创建词云对象
wc = WordCloud(
    background_color="white", #设定背景颜色
    mask=background_img, #设定填充形状
    scale=20, #设定缩放数值，数值越大图片越清晰，但生成图像速度会变慢
    font_path=getPath(ROOT, "Songti.ttc") #指定字体路径，否则中文会显示乱码
)

#2. 创建词云数据以及映射颜色
wc.generate_from_frequencies(wordsCounter) #从词频中绘制数据
img_colors = ImageColorGenerator(background_img) #将背景图颜色映射到每个词中

#3. 绘图
plt.figure(figsize=(13,8)) #在展示中的形状大小
plt.axis('off') #关闭坐标轴

#4. 导出图片
wc.to_file(getPath(ROOT, "wordcloud.jpg")) #导出图片
