from vpython import *
g=[]
s=vector(0.04,0.04,0.04)
a=box(pos=vector(-1,0,0),size=s)
b=box(pos=vector(1,0,0),size=s)
c=box(pos=vector(0,1,0),size=s)
d=box(pos=(a.pos+b.pos)/2,size=s)
e=box(pos=(b.pos+c.pos)/2,size=s)
f=box(pos=(c.pos+a.pos)/2,size=s)
g.append(a)
g.append(b)
g.append(c)
# g.append(d)
# g.append(e)
# g.append(f)
length=len(g)-1
N=10
f=[a,b,c]
n=0
while n<N :
    ran=vector(random(),random(),random())
    if ran.y<ran.x +1 or ran.y<-ran.x-1 or ran.y>-1:
        cylinder(pos=ran,axis=norm(ran),radius=0.001,color=ran)

        n+=1
    continue