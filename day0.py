from turtle import *

speed(5)
width(10)  
color("purple")


forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()



penup()
color("blue")
goto(10, 100)
pendown()
width(3)

setheading(0)  


begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



penup()
goto(135, 100)
pendown()

setheading(0)
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

exitonclick()