# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:07:20 2022

@author: wooji
"""

import turtle
t = turtle.Turtle()
t.shape("turtle")

size1 = 200
size2 = 50
move_length = 10

t.dot(size1*2, "green")

for i in range(0,301,move_length):
    print("move",i)
    t.fd(move_length)
    d = t.distance(0,0)
    print("거북이 위치: ",t.pos())
    print("원점까지의 거리(거북이): ", d)
    
    if(d == 0):
        print("충돌/동심원")
    if(size1 - size2 > d):
        print("충돌/내부존재")
    elif(size1 - size2 == d):
        print("충돌/내접")
    elif(size1 - size2 < d < size1 + size2 ):
        print("충돌/두접점")
    elif(size1 + size2 == d):
        print("충돌/외접")
    elif(size1 + size2 < d):
        print("비충돌")
    else:
        print("불가능")

t.dot(size2*2, 'blue')
turtle.exitonclick()
turtle.bye()