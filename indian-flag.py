import turtle
from turtle import*

# new turtle Instance
t = turtle.Turtle()
speed(0) #fastest

# Small Blue Circle
t.color("navy")
t.penup()
t.goto(0, 160)
t.pendown()

# thick border of chakra
t.width(4)
t.circle(50)

# 24 spokes of ashok chakra
t.penup()
t.goto(0, 210)
t.pendown()
t.pensize(2)

for i in range(24):
    t.forward(50)
    t.backward(50)
    t.left(15)

# Orange Rectangle
t.penup()
t.goto(-250, 375)
t.pendown()

t.color("orange")
t.begin_fill()
t.forward(500)
t.right(90)
t.forward(110)
t.right(90)
t.forward(500)
t.end_fill()
t.left(90)
t.forward(110)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(110)
t.left(90)
t.forward(500)
t.left(90)
t.forward(110)
t.end_fill()

# Now start the flag mast
t.penup()
t.goto(-250, 380)
t.pendown()

t.color("saddle brown")
t.width(10)
t.right(90)
t.right(90)
t.forward(600)

t.penup()
t.goto(-300, -220)
t.pendown()

# flag mast decorated 
t.begin_fill()
t.left(90)
t.forward(100)
t.right(90)
t.forward(20)
t.left(90)
t.forward(30)
t.right(90)
t.forward(20)
t.left(90)
t.forward(30)
t.right(90)
t.forward(20)
t.right(90)
t.forward(220)
t.right(90)
t.forward(20)
t.right(90)
t.forward(30)
t.left(90)
t.forward(20)
t.right(90)
t.forward(30)
t.left(90)
t.forward(20)
t.end_fill()
turtle.done()



	