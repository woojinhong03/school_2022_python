# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:50:11 2022

@author: wooji
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")

pl = [[0,0],
      [0,0],
      [0,0]]
vl = [[-2,0],
      [0,2],
      [-2,2]]

tl = []

for i in range(len(pl)):
    t = turtle.Turtle()
    t.shape("turtle")
    tl.append(t)
    
for i in range(100):
    for i in range(len(pl)):
        pl[i][0] = pl[i][0] + vl[i][0]
        pl[i][1] = pl[i][1] + vl[i][1]
        
        tl[i].goto(pl[i][0], pl[i][1])

turtle.exitonclick()
turtle.bye()

#%%

import turtle

def outline():
    tline = turtle.Turtle()
    
    tline.up()
    tline.goto(w/2,h/2)
    tline.down()

    tline.goto(-w/2,h/2)
    tline.goto(-w/2,-h/2)
    tline.goto(w/2,-h/2)
    tline.goto(w/2,h/2)
    
w = 400
h = 300

outline()

turtle.exitonclick()
turtle.bye()

#%%

from PIL import Image
image = Image.open('C:/Users/wooji/Desktop/school/python/school_2022_python/pet02.gif')
photo = image.convert('RGB')

photoAry=[]
h = photo.height
w = photo.width
for i in range(h):
    for k in range(w):
        r,g,b = photo.getpixel((i,k))
        value = (r + g + b) // 3
        photoAry.append(value)
        
dataAry = photoAry[:]
dataAry.sort()
value1 = dataAry[int(h*w / 4 * 3)]
value2 = dataAry[int(h*w / 4 * 2)]
value3 = dataAry[int(h*w / 4)]
        
for i in range(len(photoAry)):
    if photoAry[i] <= value3:
        photoAry[i] = 0
    elif photoAry[i] <= value2:
        photoAry[i] = 85
    elif photoAry[i] <= value1:
        photoAry[i] = 170
    else :
        photoAry[i] = 255

pos = 0
px = photo.load()
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1
        px[i,k] = (r,g,b)
        

photo.show()
