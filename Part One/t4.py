import turtle
turtle.setup(800,600,100,100)
turtle.pensize(5)
turtle.pencolor("black")
for i in range(4):
    turtle.seth(-90*i)
    turtle.fd(150)
    turtle.seth(-90*(i+1))
    turtle.circle(-150,45)
    turtle.goto(0,0)
turtle.done()