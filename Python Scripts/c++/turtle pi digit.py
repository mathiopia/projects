import turtle
import math
t=turtle.Turtle()
t.color('green')
t.speed(0)
n=math.pi*10
for i in range(500):
    
    m=n%10
    n=n*10
    t.forward(10*m)
    t.left(135)

    


turtle.done()