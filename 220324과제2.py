# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:07:20 2022

@author: wooji
"""

import turtle
t = turtle.Turtle()
t.shape("turtle")

x = 100
y = 50
size1 = 200
size2 = 50

print("원점에서의 거리(계산):",  ((x**2 + y**2)**0.5) ) # 예제

t.dot(size1*2, "green")
t.fd(x)
t.left(90)
t.fd(y)
t.dot(size2*2, "blue")

print("거북이 위치: ",t.pos())
print("원점까지의 거리(거북이): ", t.distance(0,0))

print("충돌 판단=>")
if(size1 - size2 > t.distance(0,0)):
    print("충돌/내부위치")
elif(size1 - size2 == t.distance(0,0)):
    print("충돌/접점존재")
elif(size1 - size2 < t.distance(0,0) < size1 + size2 ):
    print("충돌/접점존재")
elif(size1 + size2 == t.distance(0,0)):
    print("충돌/접점존재")
else:
    print("비충돌")


turtle.exitonclick()
turtle.bye()