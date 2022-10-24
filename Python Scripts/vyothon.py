from vpython import *
graph(xtitle='position',ytitle='velocity')
my_curve=gcurve(color=color.blue,)
my_sphere=sphere(pos=vector(0,0,0),radius=0.25,color=color.green,make_trail=True,trail_color=color.white,retain=50)
time=0
dt=0.5
while (time<=10):
    rate(1)
    my_sphere.pos.x+=dt
    
    time=time+1
    mycurve.plot(pos=(time,  my_sphere.pos.x))
    dt/=2
    
print ('end of program')


