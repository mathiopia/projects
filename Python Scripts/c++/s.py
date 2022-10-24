from vpython import *
coaster=curve(pos[vector(0,5,0),vector(1,4,0),vector(2,3,0),vector(3,3,0),vector(4,4,0),vector(5,5,0)],color=color.red)
cart=sphere(pos=coaster.point(0).radius,color=color.cyan,radius=0.1,mass=1,speed=0)
g=9.81
def track(posn):
    x=posn.x
    z=posn.z
    y=0
    for i in range(coaster.npoints-1):
        if coaster.point(i).pos.x<=x<=coaster.point(i+1).pos.x and coaster.point(i).pos.z<=x<=coaster.point(i+1).pos.z :
            slope=(coaster.point(i+1).pos.y-coaster.point(i).pos.y)/(coaster.point(i+1).pos.x-coaster.point.pos.x)
            intercept=coaster.point(i).pos.y-coaster.point(i).pos.x
            y=slope*x+intercept
            displacement=hat(coaster.point(i+1).pos.y-coaster.point(i).pos.y,coaster.point(i+1).pos.x-coaster.point(i).pos.x,coaster.point(i+1).pos.z-coaster.point(i).pos.z)
            
    out=[] 
    out.y=y           
    out.slope=slope
    out.displeceement=displacement
    return out
dt=0.1
dx=0.001
k=0
time=0
graph(title='speed of the coster',xtitle='time',ytitle='speed')
gspeed=gcurve(color=color.cyan,lable='speed')
while cart.pos<=coaster.point(coaster.npoints-1).pos.x:
    rate(10)
    trc=track(cart.pos)
    dy=dx*trc.slope
    dk=-cart.mass*g*dy
    k+=dk
    cart.speed=(k/abs(k))*sqrt(2*abs(k)/cart.mass)
    cart.pos+=cart.speed*dt*trc.displacement
    time+=dt
    gspeed.plot(time,cart.speed)


