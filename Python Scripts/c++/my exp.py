
from  vpython import*
theta=60*pi/180
floor=box(pos=vector(0,-1,0),size=vector(1,0.1,1),texture=textures.wood)
ball=sphere(radius=0.1,pos=floor.pos+vector(0,0.2,0),make_trail=True)
u=vector(0,1,0)
print(ball.pos)
time=0
m=10
g=vector(0,-9.8,0)
dt=0.1
while time<10: 
    rate(10)
    u=u+vector(0,-9.8*dt,0)
    ball.pos=ball.pos+(u*dt)-(0.5*9.8*dt**2)
    time=time +dt

