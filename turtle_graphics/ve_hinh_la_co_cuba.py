import turtle
a = turtle.Turtle()
a.shape("turtle")
turtle.bgcolor("gray")
a.speed(0)
a.penup()
a.goto(-200,200)
a.pendown()
for i in range(2):
	for i in range(2):
		a.color("blue")
		a.begin_fill()
		a.forward(480)
		a.right(90)
		a.forward(52)
		a.right(90)
		a.end_fill()
	a.right(90)
	a.forward(50)
	a.left(90)
	for i in range(2):
		a.color("white")
		a.begin_fill()
		a.forward(480)
		a.right(90)
		a.forward(52)
		a.right(90)
		a.end_fill()
	a.right(90)
	a.forward(50)
	a.left(90)
for i in range(2):
		a.color("blue")
		a.begin_fill()
		a.forward(480)
		a.right(90)
		a.forward(52)
		a.right(90)
		a.end_fill()
a.left(90)
a.backward(52)
a.color("red")
a.begin_fill()
for i in range(3):
	a.forward(252)
	a.right(120)
a.end_fill()
a.goto(-160,95)
a.right(90)
a.color('white')
a.begin_fill()
for i in range(5):
	a.forward(80)
	a.right(144)
a.end_fill()
a.penup()
a.goto(-300,300)
a.pendown()
turtle.done()