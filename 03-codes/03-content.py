# 一、
my_string = "我是一个孤独的字符串"
type(my_string)
print(my_string)

slogen = 'Hello, sspai!'
print(slogen)
slogen = "Hello, sspai!"
print(slogen)

# Error
slogen = "Hello, sspai!'
print(slogen)


# 二、

lyrics = '最美的不是下雨天，是曾与你躲过雨的屋檐。'
english = ' hELlo WoRld aaaaaa aaaaaaaa bbbbbbbb bbbbbbbb '

## 2.1 split
print(english.split())
print(lyrics.split(sep="，"))

## 2.2 replace
print('原字符串:', lyrics)
print('替换字符串:', lyrics.replace('你', '路小雨'))

## 2.3 *strip
print('去除左右两边空格:{}'.format(english.strip()))
print('去除右边空格:{}'.format(english.rstrip()))
print('去除左边空格:{}'.format(english.lstrip()))

## 2.4 join
text = ['临','兵','斗','者','皆','阵','列','在','前']
print('/'.join(text))

## 2.5 formatting
sspai = 'https://beta.sspai.com'
print('sspai url is: {}'.format(sspai))
print('sspai url is: %s' %sspai)

name = 'Jobs'
slogan = 'Stay Hungry, Stay Foolish.'
print("{name}'s slogon is '{slogan}'".format(name=name, slogan=slogan))

pi = 3.1415926 
print('pi原始值：%s' %pi)
print('pi保留两位小数：%.2f' %pi)

print(f"1 + 1 = {1+1}")
words = "Stay hungry, Stay foolish"
print(f"Jobs said '{words}'")


# 三、

lyrics = " sa秋刀鱼 snsk!@# 的滋味，catM 猫和你 ksd 都 sds 想123128541了解。"
english = 'hello$world!this-is=__sspai'

import re 
words = re.findall(r'[\u4e00-\u9fa5]', lyrics)
print(''.join(words))

re.split(r'[\$\!-=_]', english) #1

context = '''
白日*&%……依山尽，！@#@黄河！@#￥#入海流。\n
0001203sspAi21323233434\n
aksje!@2#jkdc11dskfd00((***))\n
'''

pattern = re.compile(
    r"""
    [\u4e00-\u9fa5]+ | #匹配中文
    [a-zA-Z]+ | #匹配英文
    [0-9]+ #匹配数字
    """, re.X) #1

pattern.findall(context) #2
