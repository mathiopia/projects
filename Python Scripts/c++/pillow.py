from PIL import Image,ImageDraw
import random
def generate_art():
    print ('generate art')
    image_size=128
    image_color=255,255,255
    image=Image.new("RGB",(image_size,image_size),(image_color))
   
    #draw some lines 
    draw=ImageDraw.Draw(image)
    for i in range (10):
        random_point_1=((random.randint(0,image_size)),(random.randint(0,image_size)))
        random_point_2=((random.randint(0,image_size)),(random.randint(0,image_size)))
        random_color_1=random.randint(0,255)
        random_color_2=random.randint(0,255)
        random_color_3=random.randint(0,255)
        linexy=(random_point_1,random_point_2)
        line_color=random_color_1,random_color_2, random_color_3 
        draw.line(linexy,fill=( line_color))
    image.save('test.png')
if __name__=="__main__":
    generate_art()