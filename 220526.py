# -*- coding: utf-8 -*-

#필요한 패키지 임포트
import sys, pygame, time

#창 제목 설정
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



loc_ship = [sw/2,sh/2]
size_ship = 25

loc_rock = [[200,200],
            [200,200],
            [200,200],
            [200,200],
            [200,200]]

vel=[[-5,5],
    [8,-5],
    [-7,-5],
    [-5,8],
    [7,-2]]

size_rock = 10

myFont = pygame.font.SysFont("arial",30,True,False)

def collision_check(loc_rock,size_rock,loc_ship,size_ship):
    dist_x = loc_rock[0] - loc_ship[0]
    dist_y = loc_rock[1] - loc_ship[1]
    dist = (dist_x**2 + dist_y**2)**(0.5)
    
    if dist < (size_rock + size_ship):
        time_diff = str(time.time() - startTime)
        print("생존 시간 : ",time_diff[:4],"초")
        pygame.quit() 
        sys.exit()


while True:
    clock.tick(30)
    screen.fill((0,0,0))
    
    for i in range(len(loc_rock)):
        pygame.draw.circle(screen,(0, 255, 0), loc_rock[i], size_rock,2)
    
    for i in range(len(loc_rock)):

        loc_rock[i][0]+=vel[i][0]
        loc_rock[i][1]+=vel[i][1]

        if loc_rock[i][0] >= sw:
            vel[i][0] = -vel[i][0]
            
        if loc_rock[i][0] <= 0:
            vel[i][0] = -vel[i][0]       
        
        if loc_rock[i][1] >= sh:
            vel[i][1] = -vel[i][1]
        
        if loc_rock[i][1] <= 0:
            vel[i][1] = -vel[i][1]
        
        collision_check(loc_rock[i], size_rock, loc_ship, size_ship)    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        loc_ship[0] -= 5
    if keys[pygame.K_RIGHT]:
        loc_ship[0] += 5
    if keys[pygame.K_UP]:
        loc_ship[1] -= 5
    if keys[pygame.K_DOWN]:
        loc_ship[1] += 5
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
    time_diff = str(time.time() - startTime)
    
    currenTime_text = myFont.render(time_diff[:4], 1, (255, 255, 255)) # 글씨 내용 저장
    screen.blit(currenTime_text, [sw-90, 20]) 
    
    pygame.draw.circle(screen, (255,255,255), loc_ship, size_ship, 4)
    x = loc_ship[0] - img_width/2
    y = loc_ship[1] - img_height/2
    screen.blit(imgShuttle, (x,y))
    
    pygame.display.update()