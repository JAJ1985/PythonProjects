import turtle
tur=turtle.Turtle()
scr=turtle.Screen()
scr.bgcolor('black')
tur.pencolor('white')
x=0
y=0
tur.speed(0)
tur.penup()
tur.goto(0,200)
tur.pendown()
while True:
	tur.forward(x)
	tur.right(y)
	x+=3
	y+=1
	turtle.done()
