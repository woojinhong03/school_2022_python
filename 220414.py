# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:29:05 2022

@author: wooji
"""

import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

square(100)
t.up()
t.goto(200,0)
t.down()
square(100)

turtle.exitonclick()
turtle.bye()

