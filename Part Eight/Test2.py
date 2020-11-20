num = eval(input())
if type(num) == "class 'float'" or type(num) == "class 'complex'" or type(num) == "class 'int'":
    print(num**2)
else:
    print("输入有误")