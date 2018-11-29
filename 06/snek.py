from turtle import *

title("Please wait>>>creating your snail<<<")
color("red")
for snek in range(16):
	circle(-12* snek, 60)
left(120)
color("orange")
forward(120)
left(90)
color("yellow")
forward(90)
left(90)
color("green")
circle(-20, 355)
left(85)
color("blue")
forward(90)
left(90)
color("purple")
forward(40)
color("blue")
circle(-20, 180)
color("green")
forward(600)
right(170)
color("yellow")
forward(210)


title("It is done, Press F to pay respect")

exitonclick()