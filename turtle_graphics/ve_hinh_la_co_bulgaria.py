import turtle
a = turtle.Turtle()
a.shape("turtle")
turtle.bgcolor("gray")
a.speed(0)
a.penup()
a.goto(-200,200)
a.pendown()
a.color("white")
a.begin_fill()
for i in range(3):
	a.fd(400)
	a.rt(90)
	a.fd(86)
	a.rt(90)
a.end_fill()
a.color("green")
a.begin_fill()
for i in range(3):
	a.fd(400)
	a.lt(90)
	a.fd(86)
	a.lt(90)
a.end_fill()
a.color("red")
a.begin_fill()
for i in range(3):
	a.fd(400)
	a.rt(90)
	a.fd(86)
	a.rt(90)
a.end_fill()
a.penup()
a.goto(-300,300)
a.pendown()
turtle.done()