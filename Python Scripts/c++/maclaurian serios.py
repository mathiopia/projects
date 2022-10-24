from vpython import * 
graph()
f=gcurve(color=color.cyan)
g=gcurve(color=color.red)
time=0
dt=0.01
while time<10:
    fu=sin(time)
    f.plot(time,fu)
    time+=dt
def f(n):
    factorial=1
    for i  in range (n):
        factorial=factorial*i
    return factorial

gx=[]
time=0
dt=0.01
while time<10:
    for i in range (10):
        gx.append(((-1)**(i+1))*(time**(2*i-1))/f(2*i-1))
        g.plot(time,g[i])

    time+=dt