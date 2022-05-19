# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:37:00 2022

@author: user
"""

import turtle

def outline():
    tline = turtle.Turtle()
    
    tline.up()
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.down()
    
    tline.goto(-SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

outline()

a = turtle.Turtle()
a.shape("circle")

loc = [100,100]
vel = [4,-4]

a.goto(loc[0], loc[1])

for i in range(200):
    loc[0] = loc[0] + vel[0]
    loc[1] = loc[1] + vel[1]
    
    if loc[0] >= SCREEN_WIDTH/2:
        loc[0] = SCREEN_WIDTH/2*2 - loc[0]
        vel[0] = -vel[0]
        
    if loc[1] <= -SCREEN_HEIGHT/2:
        loc[1] = -SCREEN_HEIGHT/2*2 - loc[1]
        vel[1] = -vel[1]
        
    a.goto(loc[0], loc[1])
    
turtle.exitonclick()
turtle.bye()

#%%
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:37:00 2022

@author: user
"""

import turtle
import time

def outline():
    tline = turtle.Turtle()
    
    tline.up()
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.down()
    
    tline.goto(-SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    tline.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

outline()

pos_list = [[0,0],
            [0,0]]
vel_list = [[5,5],
            [5,-5]]
t_list = []

startTime = time.time()

for i in range(len(pos_list)):
    t = turtle.Turtle()
    t.shape("turtle")
    t.goto(pos_list[i][0],pos_list[i][1])
    t_list.append(t)
    
for step in range(200):
    for i in range(len(pos_list)):
        pos_list[i][0] = pos_list[i][0] + vel_list[i][0]
        pos_list[i][1] = pos_list[i][1] + vel_list[i][1]

        t_list[i].goto(pos_list[i][0], pos_list[i][1])
        
        if pos_list[i][0] >= SCREEN_WIDTH/2:
            vel_list[i][0] = -vel_list[i][0]

        if pos_list[i][0] <= -SCREEN_WIDTH/2:
            vel_list[i][0] = -vel_list[i][0]
            
        if pos_list[i][1] >= SCREEN_HEIGHT/2:
            vel_list[i][1] = -vel_list[i][1]
            
        if pos_list[i][1] <= -SCREEN_HEIGHT/2:
            vel_list[i][1] = -vel_list[i][1]

timeDiff = (time.time() - startTime)    
turtle.write(timeDiff)
turtle.exitonclick()
turtle.bye()
