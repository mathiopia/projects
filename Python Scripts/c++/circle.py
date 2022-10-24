
from vpython import *
graph (xtitle="time",ytitle="position",fast=False)
mycurve=gcurve(color=color.red)
time=0
dx=0.01
ball=sphere(radius=0.1,make_trail=True)
while (time<100):
    rate(10)
    time=time+0.1
    ball.pos.x=cos(time)
    ball.pos.y=sin(time)
    mycurve.plot(time,ball.pos.y)
