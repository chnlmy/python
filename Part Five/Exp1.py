import turtle
import time
def DrawGap():
    turtle.penup()
    turtle.fd(5)
def DrawLine(draw):
    DrawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    DrawGap
    turtle.right(90)
def DrawDigit(digit):
    DrawLine(True) if digit in [2,3,4,5,6,8,9,'a','b','d','e','f'] else DrawLine(False)
    DrawLine(True) if digit in [0,1,3,4,5,6,7,8,9,'a','b','d'] else DrawLine(False)
    DrawLine(True) if digit in [0,2,3,5,6,8,9,'b','c','d','e'] else DrawLine(False)
    DrawLine(True) if digit in [0,2,6,8,'a','b','c','d','e','f'] else DrawLine(False)
    turtle.left(90)
    DrawLine(True) if digit in [0,4,5,6,8,9,'a','b','c','e','f'] else DrawLine(False)
    DrawLine(True) if digit in [0,2,3,5,6,7,8,9,'a','c','e','f'] else DrawLine(False)
    DrawLine(True) if digit in [0,1,2,3,4,7,8,9,'a','d'] else DrawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def DrawData(data):
    for i in data:
        if ord('0') <= ord(i) <= ord('9'):
            DrawDigit(eval(i))
        elif ord('a') <= ord(i) <= ord('f'):
            DrawDigit(i)
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    DrawData(time.strftime('%Y%m%d',time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()
