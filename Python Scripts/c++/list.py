from vpython import *
box_list=[]
for x in range (-2,3):
    box_list.append(box(pos=vector(x,0,0),size=vector(0.2,0.2,0.2)))
# for b in box_list:
#     print(b.pos.x)
# box_list[2].visible=False
# del box_list[2]
my_sphere=[] 
for i in range (-2,3):
    my_sphere.append(sphere(pos=vector(i,-1,0),radius=0.1))
# all_list=my_sphere+box_list