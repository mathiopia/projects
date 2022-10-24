from tkinter import N
from vpython import *
charge=sphere(radius=0.001,color=color.red)
charge.q=1e-9
escale=1e-7
k=9e9
n=10
R=0.01
dtheta=2*pi/n
theta=0
while theta<2*pi:
    r=R*vector(cos(theta),sin(theta),0)
    E=k*charge.q*norm(r)/mag(r)**2
    arrow(pos=r,axis=escale*E,color=color.yellow)
    theta+=dtheta
 
