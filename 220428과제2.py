# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:54:04 2022

@author: wooji
"""
import turtle

aList = []

for i in range(4):
    a1 = turtle.Turtle()
    a1.shape("turtle")
    aList.append(a1)

for i in range(4):
    aList[i].left(90*i)
    
    for j in range(4):
        aList[i].fd((i*40)+40)
        aList[i].left(90)
        
turtle.exitonclick()
turtle.bye()