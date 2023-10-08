import turtle

window = turtle.Screen()
pen = turtle.Turtle()

window.setup(width=450, height=400)
window.bgcolor("light green")
window.title("Star")

pen.pencolor("black")
pen.penup()
pen.goto(0 ,150)
pen.pendown()

pen.fillcolor("light blue")
pen.begin_fill()

pen.right(75)
pen.forward(300)
 
for i in range(4):
    pen.right(144)
    pen.forward(300)
     
pen.end_fill()

pen.penup()
pen.goto(29,-23)
pen.pendown()
pen.pencolor("black")
pen.fillcolor("light green")
pen.begin_fill()
pen.circle(40)
pen.end_fill()


pen.hideturtle()
turtle.done()
screen.exitonclick()