import turtle as t
import time

# scr = t.Screen()
t.color("orange","black")
# scr.bgcolor("")
t.pensize(3)

for i in range(0,10):
    t.right(-36)
    for i in range(0,5):
        t.forward(100)
        t.right(72)

time.sleep(3)
t.bye()