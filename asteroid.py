# -*- coding: utf-8 -*-

#필요한 패키지 임포트
import sys, pygame, time

#창 제목 설정
pygame.init()
pygame.display.set_caption('Space')

#창 사이즈 지정
sw = 640
sh = 480
screen = pygame.display.set_mode((sw, sh))

#로켓 생성
imgShuttle = pygame.image.load('rocket.png')
img_width = imgShuttle.get_width()
img_height = imgShuttle.get_height()

#시간측정을 위한 시간 생성, 딜레이 생성
clock = pygame.time.Clock()
startTime = time.time()

#소행성과 로켓 설정 
loc_ship = [sw/2,sh/2]
size_ship = 25

size_rock = 10
loc_rock = [[200,200],
            [200,200],
            [200,200],
            [200,200],
            [200,200],
            [200,200],
            [200,200]]
vel = [[-5,5],
       [8,-5],
       [-7,-5],
       [-5,8],
       [7,-2],
       [8,8],
       [-2,9]]

#폰트 설정 
myFont = pygame.font.SysFont("arial",30,True,False)

#충돌 판단 함수 
def collision_check(loc_rock,size_rock,loc_ship,size_ship):
    dist_x = loc_rock[0] - loc_ship[0]
    dist_y = loc_rock[1] - loc_ship[1]
    dist = (dist_x**2 + dist_y**2)**(0.5)
    
    #충돌 시 충돌시간 프린트, 종료
    if dist < (size_rock + size_ship):
        time_diff = str(time.time() - startTime)
        print("생존 시간 : ",time_diff[:4],"초")
        pygame.quit() 
        sys.exit()


while True:
    clock.tick(40)
    screen.fill((0,0,0))
    
    #소행성 생성
    for i in range(len(loc_rock)):
        pygame.draw.circle(screen,(0, 255, 0), loc_rock[i], size_rock,2)
    
    #소행성 움직이게 만들기
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
        
        #충돌함수 호출
        collision_check(loc_rock[i], size_rock, loc_ship, size_ship)    
    
    #키 입력 시 로켓 움직이게 만들기 
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        loc_ship[0] -= 5
        
    if keys[pygame.K_RIGHT]:
        loc_ship[0] += 5
        
    if keys[pygame.K_UP]:
        loc_ship[1] -= 5
        
    if keys[pygame.K_DOWN]:
        loc_ship[1] += 5
        
    #q 눌렀을 때 종료 
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
    #실행시간 출력
    time_diff = str(time.time() - startTime)
    currenTime_text = myFont.render(time_diff[:4], 1, (255, 255, 255))
    screen.blit(currenTime_text, [sw-90, 20]) 
    
    #로켓 생성 
    pygame.draw.circle(screen, (255,255,255), loc_ship, size_ship, 4)
    x = loc_ship[0] - img_width/2
    y = loc_ship[1] - img_height/2
    screen.blit(imgShuttle, (x,y))
    
    pygame.display.update()