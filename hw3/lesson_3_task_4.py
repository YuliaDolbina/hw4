import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(8)
t.penup()
t.goto(0,-100)
t.pendown()

for i in range(36):
    t.forward(30)
    t. left(10)

t.penup()
t.goto(-80,90)
t.pendown()
t.left(90)
for i in range(45):
    t.forward(2)
    t.right(4)
t.penup()
t.goto(50,90)
t.pendown()

t.left(-180)
for i in range(45):
    t.forward(2)
    t.right(4)

t.penup()
t.goto(0,50)
t.pendown()
t.setheading(0)
for i in range(5):
    t.forward(25)
    t.right(120)
starting_nose_x = t.xcor()
starting_nose_y = t.ycor()

t.left(120)
t.forward(10)
for i in range(4):
    t.right(16)
    t.forward(17)
    
t.penup()
t.goto(starting_nose_x, starting_nose_y)    
t.pendown()
t.setheading(-60)

t.forward(10)
for i in range(4):
    t.left(16)
    t.forward(17)

t.screen.exitonclick()   