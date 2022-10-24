from vpython import *
R=1
dr=0.01
N=1000
A=4*pi*R**2/N
n=0
s=vector(random(),random(),random())

while n<N:
    rt=R*vector(random(),random(),random())
    a=-R*vector(random(),random(),random())
    b=vector(-R*random(),random(),random())
    c=R*vector(-R*random(),-R*random(),random())
    d=R*vector(random(),-R*random(),random())
    e=R*vector(random(),-R*random(),-R*random())
    f=R*vector(random(),random(),-R*random())
    g=R*vector(-R*random(),random(),-R*random())
    if mag(rt)<R+dr and mag(rt)> R-dr:
        cylinder(pos=rt,axis=dr*norm(rt),radius=sqrt(A/pi)/1.2,color=vector(random(),random(),random()))

        n+=1
    if mag(a)<R+dr and mag(a)> R-dr:
        cylinder(pos=a,axis=dr*norm(a),radius=sqrt(A/pi)/1.2,color=vector(random(),random(),random()))

        n+=1
    if mag(b)<R+dr and mag(b)> R-dr:
        cylinder(pos=b,axis=dr*norm(b),radius=sqrt(A/pi)/1.2,color=vector(random(),random(),random()))

        n+=1
    if mag(c)<R+dr and mag(c)> R-dr:
        cylinder(pos=c,axis=dr*norm(c),radius=sqrt(A/pi)/1.2,color=vector(random(),random(),random()))

        n+=1
    if mag(d)<R+dr and mag(d)> R-dr:
        cylinder(pos=d,axis=dr*norm(d),radius=sqrt(A/pi)/1.2,color=vector(random(),random(),random()))

        n+=1
    if mag(e)<R+dr and mag(e)> R-dr:
        cylinder(pos=e,axis=dr*norm(e),radius=sqrt(A/pi)/1.2,color=vector(random(),random(),random()))

        n+=1
    if mag(f)<R+dr and mag(f)> R-dr:
        cylinder(pos=f,axis=dr*norm(f),radius=sqrt(A/pi)/1.2,color=vector(random(),random(),random()))

        n+=1
    if mag(g)<R+dr and mag(g)> R-dr:
        cylinder(pos=g,axis=dr*norm(g),radius=sqrt(A/pi)/1.2,color=vector(random(),random(),random()))

        n+=1