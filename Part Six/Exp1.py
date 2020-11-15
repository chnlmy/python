def getNum():       #获取用户不定长度的输入
    nums = []
    str1 = input()
    inums = str1.split(sep=',')
    for i in inums:
        nums.append(eval(i))
    return nums


def mean(numbers):  #计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s/len(numbers)
    
def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):    #计算中位数
    new = sorted(numbers)
    if len(numbers) % 2 == 0:
        mid = (new[len(numbers)//2-1] + new[len(numbers)//2])/2
    else:
        mid = new[len(numbers)//2]
    return mid
    
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m, dev(n,m), median(n)))