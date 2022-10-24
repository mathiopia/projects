from vpython import *
me=5.972e24
re=6.378e6
G=6.67e-11
we=7.3e-5
earth=sphere(radius=re,texture=textures.earth)
# earth.rotate(angle=pi/2,axis=vector(1,0,0),origin=earth.pos)
rc=(G*me/we**2)**(1/3)
craft=sphere(pos=vector(rc,0,0),radius=re/20,color=color.yellow,make_trail=True)
craft.m=1000
vc=sqrt(G*me/rc)
craft.p=craft.m*vc*vector(0,1,0)
time=0
dt=100
day=24*3600
while time<=2*day:
    rate(100)
    earth.rotate(angle=we*dt,axis=vector(0,0,1),origin=earth.pos)
    r=craft.pos-earth.pos
    F=-G*craft.m*me*norm(r)/mag(r)**2
    craft.p=craft.p+F*dt
    craft.pos=craft.pos+(craft.p/craft.m)*dt
    time+=dt