height, weight = eval(input())
BMI = weight / height ** 2
print("BMI数值为：{:.2f}".format(BMI))
IB = ' '
GB = ' '
if BMI < 18.5:
    IB = '偏瘦'
    GB = '偏瘦'
elif BMI < 24:
    IB = '正常'
    GB = '正常'
elif BMI < 25:
    IB = '正常'
    GB = '偏胖'
elif BMI < 28:
    IB = '偏胖'
    GB = '偏胖'
elif BMI < 30:
     IB = '偏胖'
     GB = '肥胖'
else:
    IB = '肥胖'
    GB = '肥胖'
print("BMI指标为：国际'{0}'，国内'{1}'".format(IB, GB))