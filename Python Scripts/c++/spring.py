from curses.panel import top_panel
from vpython import *
m=0.1
k=10.5
lo=0.07
g= vector(0,-9.8,0)
top=sphere(pos=vector(0,lo,0),radius=0.004)
mass=sphere(pos=top.pos-vector(0.3*lo,lo,0),radius=0.01,color=color.yellow,make_trail=True)
spring=helix(radius=0.004,pos=top.pos,axis=mass.pos-top.pos,thickness=0.003)
mass.p=m*vector(1,0,0)
# attach_arrow(mass,'p')
time=0
dt=0.01
while time<10:
    rate(70)
    spring.axis=mass.pos -top.pos
    l=mass.pos-top.pos
    F=(-k*(mag(l)-lo)*norm(l))+m*g
    mass.p+=F*dt
    mass.pos+=(mass.p/m)*dt
    time=time+dt