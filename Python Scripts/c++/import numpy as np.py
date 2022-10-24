import numpy as np
import matplotlib.pyplot as plt

def f(c,z):
    return z**2+c
c=complex(1,2)
def diverge(c,n=20,b=20000,z=0):
    c=complex(*c)
    for i in range(n):
        z=f(c,z)
        if abs(z)>b:return 1
            
    return 0
xmin,xmax=-2,1
ymin,ymax=-1,1
res=200

xx,yy=np.meshgrid(np.linspace(xmin,xmax,res),np.linspace(ymin,ymax,res))
points=np.c_[xx.ravel(),yy.ravel()]
mandlbrot=[diverge(c)for c in points]
mandlbrot=np.array(mandlbrot)
mandlbrot=np.reshape(200,200)
plt.imshow(mandlbrot)