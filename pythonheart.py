import turtle
import time

screen=turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("#eb818f")

#creates a turtle object
t=turtle.Turtle()
t.speed(5)
t.hideturtle()

#drawheart
def draw_heart():
    t.penup()
    t.goto(0,-150)
    t.pendown()
    t.begin_fill()
    t.fillcolor("pink")
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

draw_heart()

def animate_text(text,start_position,font=("Arial",15,"bold"),color="white",delay=0.1):
    x, y = start_position
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    for char in text:
        t.write(char, align="center",font=font)
        x += 15
        t.penup()
        t.goto(x,y)
        t.pendown()
        time.sleep(delay)

while(1):
    animate_text("Happy Valentine's Day!!", (-150, 0))
    t.clear()
    t.setheading(0)
    t.pencolor("white")
    draw_heart()

turtle.done()
