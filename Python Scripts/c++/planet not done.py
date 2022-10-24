from vpython import *
import math
AU=149.6e6*1000
G=6.67428e-11
# SCALE=250/AU #1Au=100 pixels
TIME_STEPS=3600*24 # 1day
# sun=Planet(0,0,30,YELLOW,1.98892e30)
    
#earth=Planet(-1 *Planet. AU,0,16,BLUE,5.9742e24)
#earth.y_vel=29.783e3
#mars=Planet(-1.524*Planet.AU,0,12,RED,6.39e23)
# mars.y_vel=24.077e3
# mercury=Planet(0.387*Planet.AU,0,8,GREEN,0.33e24)        
# mercury.y_vel=47.3e3
# venus=Planet(0.723*Planet.AU,0,14,WHITE,4.8685e24)
# venus.y_vel=-35.02e3
sun=sphere(mass=1.98892e30,radius=8963*1000,pos=vector(0,0,0),color=color.orange )
sun.angular_velocity=2.865329e-6

mercury=sphere(mass=0.33e24,orbital_radius=57.9e6,radius=2440*1000,pos=vector(57.9e6,0,0),color=color.yellow,make_trail=True)
mercury.angular_velocity=1.2397e-6
mercury.orbital_velocity=47.4*1000

venus=sphere(mass=4.8685e24,orbital_radius=108.2e6,radius=6052*1000,pos=vector(108.2e6,0,0),color=color.cyan,make_trail=True)
venus.angular_velocity=2.992e-7
venus.orbital_velocity=35*1000

earth=sphere(mass=5.9742e24,orbital_radius=149.6e6,radius=6371*1000,pos=vector(149.6e6,0,0),texture=textures.earth,make_trail=True)
earth.angular_velocity=7.292115e-5
earth.orbital_velocity=29.8*1000

mars=sphere(mass=6.39e23,orbital_radius=228e6,radius=3390*1000,pos=vector(228e6,0,0),color=color.red,make_trail=True)
mars.angular_velocity=7.088218e-5
mars.orbital_velocity=24.1*1000
time=0
dt=100
year=365*24*3600
planets=[mercury,venus,earth,mars]
t_force=0
t_force_x=0
t_force_z=0
for i  in planets:
    for j in planets:
        if i!=j:
            distance_x=i.pos.x-j.pos.x
            distance_z=i.pos.z-j.pos.z
            distance=mag(i.pos-j.pos)
            theta=atan2(distance_x,distance_z)
            t_force+=G*i.mass*j.mass/distance**2
            t_force_x+=t_force*cos(theta)
            t_force_z+=t_force*sin(theta)





while time<2*year:
    rate(100)
    

    mercury.rotate(angle=mercury.angular_velocity*dt,axis=vector(0,0,1),origin=mercury.pos)
    mercury.orbital_velocity+=
    venus.rotate(angle=venus.angular_velocity*dt,axis=vector(0,0,1),origin=venus.pos)
    earth.rotate(angle=earth.angular_velocity*dt,axis=vector(0,0,1),origin=earth.pos)
    mars.rotate(angle=mars.angular_velocity*dt,axis=vector(0,0,1),origin=mars.pos)

