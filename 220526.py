# -*- coding: utf-8 -*-
import sys, pygame, time

pygame.init()
pygame.display.set_caption('Space')

sw = 640
sh = 480

screen = pygame.display.set_mode((sw, sh))

imgShuttle = pygame.image.load('rocket.png')
img_width = imgShuttle.get_width()
img_height = imgShuttle.get_height()

clock = pygame.time.Clock()
startTime = time.time()

loc_rock = [100,100]
size_rock = 10

loc_ship = [sw/2,sh/2]
size_ship = 20

myFont = pygame.font.SysFont("arial",30,True,False)
def collision_check(loc_rock, size_rock, loc_ship, size_ship):
    dist_x = loc_rock[0] - loc_ship[0]
    dist_y = loc_rock[1] - loc_ship[1]
    dist = (dist_x**2 + dist_y**2)**(0.5)
    
    if dist < (size_rock + size_ship):
        collision_text = myFont.render("Collision",1,(255,0,0))
        screen.blit(collision_text,[20,20])

vel = [4,4]

while True:
    clock.tick(30)
    screen.fill((0,0,0))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        loc_ship[0] -= 3
    if keys[pygame.K_RIGHT]:
        loc_ship[0] += 3
    if keys[pygame.K_UP]:
        loc_ship[1] -= 3
    if keys[pygame.K_DOWN]:
        loc_ship[1] += 3
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.draw.circle(screen, (0,255,0), loc_rock, size_rock, 2)
    pygame.draw.circle(screen, (255,255,255), loc_ship, size_ship, 2)
    
    
    x = loc_ship[0] - img_width/2
    y = loc_ship[1] - img_height/2
    
    collision_check(loc_rock, size_rock, loc_ship, size_ship)
    screen.blit(imgShuttle, (x,y))
    
    pygame.display.update()