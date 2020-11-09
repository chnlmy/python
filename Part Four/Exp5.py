i = 0
while i <= 3:
    name = input()
    code = input()
    if name == 'Kate' and code =='666666':
        print("登录成功！")
        break
    else:
        i = i+1
if i == 3:
    print("3次用户名或者密码均有误！退出程序。")