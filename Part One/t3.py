import turtle
turtle.setup(800,600,100,100)
turtle.pensize(5)
turtle.pencolor("black")
for i in range(9):
    turtle.seth(i*80)
    turtle.fd(100)
turtle.done()