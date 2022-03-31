# -*- coding: utf-8 -*-

import turtle
t=turtle.Turtle()
t.shape("turtle")
t.color("blue")

x = int(input("가로:"))
y = int(input("세로:"))
angle = 90

print("원점에서의 거리(계산) : ", ((x**2 + y**2)**0.5))

t.forward(x)
t.left(90)
t.forward(y)

print("거북이 위치 : ", t.pos())
print("원점에서의 거리(거북이) : ", t.distance(0,0))

turtle.exitonclick()
turtle.bye()