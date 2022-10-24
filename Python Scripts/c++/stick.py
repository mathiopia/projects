from vpython import *
g=vector(0,-9.81,0)
floor=box(pos=vector(0,-0.5,0),texture=textures.wood,size=vector(2.5,0.1,1))
pivot=sphere(pos=floor.pos+vector(0,0.05,0),radius=0.03)
l=5
ball2=sphere(pos=pivot.pos+vector(-0.25,l,0),color=color.cyan,make_trail=True,radius=0.05)
ball2.v=vector(0,0,0)
theta=20*pi/180
ball=sphere(pos=pivot.pos+l*(vector(sin(theta),cos(theta),0)),radius=0.05,color=color.yellow,make_trail=True )
stick=cylinder(pos=pivot.pos,axis=ball.pos-pivot.pos,radius=0.03,opacity=0.5)
m=0.1
I=m*l**2
time=0
dt=0.001
w=0
while theta<pi/2:
    rate(1000)
    if ball2.pos.y < pivot.pos.y:
        ball2.v=vector(0,0,0)
    alpha=(l*m*mag(g)*sin(theta))/I
    w=w+(alpha*dt)
    theta=theta+(w*dt)
    ball.pos=pivot.pos+l*(vector(sin(theta),cos(theta),0))
    stick.axis=ball.pos-pivot.pos
    ball2.v=ball2.v+g*dt
    ball2.pos=ball2.pos+ball2.v*dt
  

    time+=dt



