import turtle

def draw_shape():
	window = turtle.Screen()
	window.bgcolor("yellow")

	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.speed(1)
	brad.color("green")
	
	for i in range(4):
		brad.forward(100)
		brad.right(90)

	angie = turtle.Turtle()
	angie.shape("turtle")
	angie.speed(1)
	angie.color("red")
	angie.circle(100)

	victor = turtle.Turtle()
	for i in range(3):
		victor.forward(80)
		victor.right(120)

	window.exitonclick()

draw_shape()