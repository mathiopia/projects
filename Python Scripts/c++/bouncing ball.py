from vpython import *
# run=False
# def runbutton(b):
#     if run:
#         b.text='run'
#     else:
#         b.text='pause'
floor=box(pos=vector(0,-5,0),size=vector(10,0.1,10),texture=textures.wood)
ball=sphere(radius=0.4,color=color.blue,make_trail=True,pos=vector(-5,5,0))
g=9.81
h=ball.pos.y
ball.m=0.5
# ball.v=sqrt(2*g*h)
ball.p=ball.m*vector(1,0,0)
time=0
dt=0.01
attach_arrow(ball,'p')
# R=ball.pos.x
while ball.pos.x<=8:
   
    rate(200)
    f=vector(0,-1*ball.m*g,0)
    ball.p=ball.p+f*dt
    ball.pos=ball.pos+(ball.p/ball.m)*dt
    if ball.pos.y<= floor.pos.y + ball.radius:
        ball.p.y=-(ball.p.y)
    time=time+dt
