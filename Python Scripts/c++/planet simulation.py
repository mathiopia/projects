import pygame
import math
pygame.init()
WIDTH,HEIGHT = 800,800
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('planet simulation')
WHITE=(255,255,255)
RED=(200,0,50)
BLUE=(0,0,255)
GREEN=(90,50,120)
YELLOW=(255,255,0)
FONT=pygame.font.SysFont('comicsans', 16)
class Planet:
    AU=149.6e6*1000
    G=6.67428e-11
    SCALE=250/AU #1Au=100 pixels
    TIME_STEPS=3600*24 # 1day
    def __init__(self,x,y,radius,color,mass):
        self.x=x
        self.y=y
        self.sun=False
        self.orbit=[]
        self.distance_to_sun=0
        self.radius=radius
        self.mass=mass
        self.color=color
        self.x_vel=0
        self.y_vel=0

    def draw(self,win):
        x=self.x*self.SCALE + WIDTH/2
        y=self.y*self.SCALE + HEIGHT/2
        
        
        if len(self.orbit)>2:
            updated_points=[]
            for points in self.orbit:
                x,y=points
                x= x*self.SCALE + WIDTH/2
                y= y*self.SCALE + HEIGHT/2
                updated_points.append ((x,y))
            pygame.draw.lines(win,self.color,False,updated_points,2)
        pygame.draw.circle(win,self.color,(x,y),self.radius)
        if not self.sun:
            distance_text=FONT.render(f"{round(self.distance_to_sun/149.6e6*1000,2)}AU",1,WHITE)
            win.blit(distance_text,(x-distance_text.get_width()/2,y-distance_text.get_height()/2))
    def Attraction(self,other):
        other_x,other_y=other.x,other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance=math.sqrt(distance_x**2 +distance_y**2)
        # if self==other:
        #     return
        if other.sun:
            self.distance_to_sun=distance
        
        force=self.G*self.mass*other.mass/distance**2
        theta=math.atan2(distance_y,distance_x)
        force_x=math.cos(theta)*force
        force_y=math.sin(theta)*force
        return force_x,force_y

    def update_position(self,planets):
        total_fx=total_fy=0
        for Planet in planets:
            if self==Planet:
                continue
            fx,fy=self.Attraction(Planet)
            total_fx+=fx
            total_fy+=fy
        self.x_vel+=total_fx/self.mass *self.TIME_STEPS
        self.y_vel+=total_fy/self.mass *self.TIME_STEPS
        self.x+=self.x_vel*self.TIME_STEPS
        self.y+=self.y_vel*self.TIME_STEPS
        self.orbit.append((self.x,self.y))


def main():
    run=True
    clock=pygame.time.Clock()
    
    sun=Planet(0,0,30,YELLOW,1.98892e30)
    sun.sun=True
    
    earth=Planet(-1 *Planet. AU,0,16,BLUE,5.9742e24)
    earth.y_vel=29.783e3
    mars=Planet(-1.524*Planet.AU,0,12,RED,6.39e23)
    mars.y_vel=24.077e3
    mercury=Planet(0.387*Planet.AU,0,8,GREEN,0.33e24)
    mercury.y_vel=47.3e3
    venus=Planet(0.723*Planet.AU,0,14,WHITE,4.8685e24)
    venus.y_vel=-35.02e3
    planets=[sun,earth,mars,mercury,venus]
    
    while run:
        clock.tick(60)
        win.fill((0,0,0))
        # win.fill(white)
        # pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        for planet in planets:
            planet.draw(win)
            planet.update_position(planets)
        pygame.display.update()
    pygame.quit()
main()


