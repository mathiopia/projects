from vpython import  *
def make_grid(xmax,dx):
    for x in range(-xmax,xmax+dx,dx):
        curve(pos=[vector(x,-xmax,0),vector(x,xmax,0)])
    for y in range(-xmax,xmax+dx,dx):
        curve(pos=[vector(-xmax,y,0),vector(xmax,y,0)])
    return
def make_3dgrid(xmax,dx):
    global grid
    grid=[]

    #xy plane
    for x in range(-xmax,xmax+dx,dx):
        grid.append (curve(pos=[vector(x,-xmax,0),vector(x,xmax,0)]))
    for y in range(-xmax,xmax+dx,dx):
         grid.append(curve(pos=[vector(-xmax,y,0),vector(xmax,y,0)]) )
    #xz plane
    for x in range(-xmax,xmax+dx,dx):
         grid.append(curve(pos=[vector(x,0,-xmax),vector(x,0,xmax)]))
    for z in range(-xmax,xmax+dx,dx):
         grid.append(curve(pos=[vector(-xmax,0,z),vector(xmax,0,z)])) 
    #yzplane
    for z in  range(-xmax,xmax+dx,dx):
         grid.append(curve(pos=[vector(0,-xmax,z),vector(0,xmax,z)]))
    for y in range(-xmax,xmax+dx,dx):
        grid.append( curve(pos=[vector(0,y,-xmax),vector(0,y,xmax)]) )
    return
def trun_grid(onoroff):
    global grid
    if onoroff == 'on':
        for shape in grid :
            shape.visible=True
    if  onoroff =='off':
        for shape in grid:
            shape.visible=False
    return
make_3dgrid(4,1)
while(True):
    rate(1)
    sleep(1)
    trun_grid("on")
    sleep(1)
    trun_grid("off")


