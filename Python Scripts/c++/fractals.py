from turtle import *
speed(0)
hideturtle()
def fate(length,levels):
    if levels==0:
        forward(length)
        return
    length/=3
    fate(length,levels-1)
    left(60)
    fate(length,levels-1)
    right(120)
    fate(length,levels-1)
    left(60)
    fate(length,levels-1)
    
fate(1000,5)


mainloop()