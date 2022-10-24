from vpython import *
roof=sphere(radius=0.05,pos=vector(0,1,0))
theta=30*pi/180
R=2
ball=sphere(pos=roof.pos+R*vector(sin(theta),-cos(theta),0),color=color.cyan,radius=0.1,make_trail=True)
string=cylinder(pos=roof.pos,axis=ball.pos-roof.pos,radius=0.02,opacity=0.3,color=color.red)
alpha=0
omega=0
g=-9.81
time=0
dt=0.01
while time<10:
    rate(100)
    alpha=(g/R)*sin(theta)
    omega+=alpha*dt
    theta+=omega*dt
    time=time+dt
    ball.pos=roof.pos+R*vector(sin(theta),-cos(theta),0)
    string.axis=axis=ball.pos-roof.pos

