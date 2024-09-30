import turtle as t

t.shape("turtle")

#To draw one.
t.left(90)
t.forward(100)
t.penup()

t.right(90)
t.forward(50)

#To draw two.
t.pendown()
t.forward(80)
t.right(90)
t.forward(50)
t.right(90)
t.forward(80)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)
t.penup()

t.forward(50)

#To draw three
t.pendown()
t.forward(80)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)
t.right(180)
t.forward(80)
t.left(90)
t.forward(50)
t.left(90)
t.forward(80)

t.exitonclick()