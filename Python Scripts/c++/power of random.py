# from scipy import random as rr
from vpython import *
R=1
dr=0.01
N=1000
A=2*pi*R**2/N
n=0
# r=rr.uniform(-R,R)
# rt=vector(r,r,r)

while n<N:
    rt=R*vector(random(),random(),random())
    if mag(rt)<R+dr and mag(rt)> R-dr:
        cylinder(pos=rt,axis=dr*norm(rt),radius=sqrt(A/pi),color=vector(random(),random(),random()))

        n+=1