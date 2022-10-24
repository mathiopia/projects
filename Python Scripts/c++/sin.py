import turtle
import math
t=turtle.Turtle()
# turtle.shape('turtle')
t.speed(0)
t.color('green')


for i in range (100):
    t.forward(10)
    t.left(50*math.sin(i/10))
    t.left(20)
# mainloop()


turtle.done()