A = pow(1.01, 365)
fact = 0.01
def improve(f):
    B = 1.0
    for i in range(365):
        if i % 7 in [6,0]:
            B = B*0.99
        else:
            B = B*(1+f)
    return B
while (improve(fact) < A):
    fact=fact+0.001
print("工作日的努力参数是{:.3f}".format(fact))