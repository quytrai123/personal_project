import turtle
a = turtle.Turtle()
a.shape("turtle")
a.getscreen().bgcolor("gray")
a.speed(0)
a.penup()
a.goto(-200,200)
a.pendown()
for i in range(7):
    a.begin_fill()
    a.color("red")
    for i in range(2):
        a.forward(470)
        a.right(90)
        a.forward(20)
        a.right(90)
    a.right(90)
    a.forward(20)
    a.left(90)
    a.end_fill()
    a.color("white")
    a.begin_fill()
    for i in range(2):
        a.forward(470)
        a.right(90)
        a.forward(20)
        a.right(90)
    a.right(90)
    a.forward(20)
    a.left(90)
    a.end_fill()
a.left(90)
a.forward(280)
a.right(90)
a.color("blue")
a.begin_fill()
for i in range(2):
    a.forward(135)
    a.right(90)
    a.forward(139)
    a.right(90)
a.end_fill()
a.color("white")
a.penup()
a.forward(10)
a.right(90)
a.forward(14)
a.left(90)
a.pendown()
a.begin_fill() 
for i in range(6):
    for i in range(5):
        a.forward(10)
        a.right(144)
    a.penup()
    a.forward(20)
    a.pendown()
a.end_fill()
a.penup()
a.backward(135)
a.forward(25)
a.right(90)
a.forward(14)
a.left(90)
a.pendown()
a.begin_fill()
for i in range(5):
    for i in range(5):
        a.forward(10)
        a.right(144)
    a.penup()
    a.forward(20)
    a.pendown()
a.end_fill()
a.penup()
a.backward(125)
a.pendown()
a.penup()
a.forward(15)
a.right(90)
a.forward(14)
a.left(90)
a.pendown()
a.begin_fill() 
for i in range(6):
    for i in range(5):
        a.forward(10)
        a.right(144)
    a.penup()
    a.forward(20)
    a.pendown()
a.end_fill()
a.penup()
a.backward(135)
a.forward(25)
a.right(90)
a.forward(14)
a.left(90)
a.pendown()
a.begin_fill()
for i in range(5):

    for i in range(5):
        a.forward(10)
        a.right(144)
    a.penup()
    a.forward(20)
    a.pendown()
a.end_fill()
a.penup()
a.backward(125)
a.pendown()
a.end_fill()
a.penup()
a.forward(15)
a.right(90)
a.forward(14)
a.left(90)
a.pendown()
a.begin_fill() 
for i in range(6):
    for i in range(5):
        a.forward(10)
        a.right(144)
    a.penup()
    a.forward(20)
    a.pendown()
a.end_fill()
a.penup()
a.backward(135)
a.forward(25)
a.right(90)
a.forward(14)
a.left(90)
a.pendown()
a.begin_fill()
for i in range(5):
    for i in range(5):
        a.forward(10)
        a.right(144)
    a.penup()
    a.forward(20)
    a.pendown()
a.end_fill()
a.penup()
a.backward(125)
a.pendown()
a.penup()
a.forward(15)
a.right(90)
a.forward(14)
a.left(90)
a.pendown()
a.begin_fill() 
for i in range(6):
    for i in range(5):
        a.forward(10)
        a.right(144)
    a.penup()
    a.forward(20)
    a.pendown()
a.end_fill()
a.penup()
a.backward(135)
a.forward(25)
a.right(90)
a.forward(14)
a.left(90)
a.pendown()
a.begin_fill()
for i in range(5):
    for i in range(5):
        a.forward(10)
        a.right(144)
    a.penup()
    a.forward(20)
    a.pendown()
a.end_fill()
a.penup()
a.backward(125)
a.pendown()
a.end_fill()
a.penup()
a.forward(15)
a.right(90)
a.forward(14)
a.left(90)
a.pendown()
a.begin_fill() 
for i in range(6):
    for i in range(5):
        a.forward(10)
        a.right(144)
    a.penup()
    a.forward(20)
    a.pendown()
a.end_fill()
a.penup()
a.goto(-300,300)
a.pendown()
turtle.done()