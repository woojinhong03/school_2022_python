# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:15:29 2022

@author: wooji
"""
import turtle
t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('blue')

t2 = turtle.Turtle()
t2.shape('turtle')
t2.color('green')

t3 = turtle.Turtle()
t3.shape('turtle')
t3.color('red')

def square(t):
    for i in range(4):
        t.fd(100)
        t.left(90)    

t1.up()
t1.goto(0,100)
t1.down()
square(t1)

t2.up()
t2.goto(300,0)
t2.down()
square(t2)

t3.up()
t3.goto(0,-200)
t3.down()
square(t3)


turtle.exitonclick()
turtle.bye()

