from vpython import *
R=1
k=100
v=0.5
m=0.05
g=vector(0,-9.81,0)
theta=0
roof=sphere(radius=0.05,pos=vector(0,1,0),opacity=0.7)
ball=sphere(pos=roof.pos+R*vector(sin(theta),-cos(theta),0),color=color.cyan,radius=0.1,make_trail=True)
string=cylinder(pos=roof.pos,axis=ball.pos-roof.pos,radius=0.02,opacity=0.3,color=color.green)
lo=R-((m*v**2)/R+m*mag(g))/k
time=0
ball.p=vector(-v,0,0)*m
dt=0.01

while time<10:
    rate(10)
    l=roof.pos-ball.pos
    fs=-k*(mag(l)-lo)*l.hat
    F=fs+m*g
    ball.p+=F*dt
    ball.pos+=(ball.p/m)*(dt)
    string.axis=ball.pos-roof.pos
    time+=dt
