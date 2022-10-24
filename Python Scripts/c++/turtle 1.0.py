import turtle
wn=turtle.Screen()
wn.title('my test')
wn.bgcolor('black')
wn.setup(width=800,height=600)
#wn.tracer(0)
t=turtle.Turtle()
t.pencolor('green')
a=0
b=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

while(True):
    #wn.update()
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b==200:
        break
    t.hideturtle()
turtle.done()