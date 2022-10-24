from turtle import*
shape('turtle')
speed(0)
def tree(size,level,angle):
    if level==0:
        # color('green')
        # dot(10)
        # color('black')
        return
    forward(size)
    right(angle)
    tree(size*0.8,level-1,0.9*angle)

    left(2*angle)

    tree(size*0.8,level-1,0.9*angle)
    right(angle)
    backward(size)
left(90)
tree(70,5,30)
mainloop()
