try:
    dic = {}
    turn = {}
    dic = eval(input())
    for i in dic:
        turn[dic.get(i)] = i
    print(turn)
except:
    print("输入错误")