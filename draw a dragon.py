import turtle
t = turtle.Turtle()
s = turtle.Screen()

# makes the head
square=1
t.color("black", "red")
t.begin_fill()
while square <4:
    
    t.forward(100)
    t.left(90)
    
    square=square +1
t.end_fill()
#eyes
t.color("black", "white")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(40)
t.left(180)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(80)
t.left(90)
t.forward(40)
t.right(90)
t.forward(10)
t.right(90)
t.forward(50)
t.left(180)
t.end_fill()
#body
t.color("black", "red")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(350)
t.left(90)
t.forward(100)
t.left(90)
t.forward(350)
t.end_fill()    


# makes the tail
t.color("black", "red")
t.begin_fill()
t.left(90)
t.forward(100)
t.left(90)
t.forward(350)
t.left(50)
t.forward(150)
t.left(90)
t.forward(25)
t.left(90)
t.forward(125)
t.right(50)
t.forward(347)
t.left(90)
t.forward(40)
t.end_fill()


# makes the legs
t.color("black", "red")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(105)
t.end_fill()


t.color("black", "red")
t.begin_fill()
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(105)
t.end_fill()


 

s.exitonclick()
