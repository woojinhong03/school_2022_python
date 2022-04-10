# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 20:03:34 2022

@author: wooji
"""
import random
import turtle

t = turtle.Turtle()

t1 = turtle.Turtle()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.shape("turtle")

t1.color("blue")
t1.goto(0,200)
t2.color("red")
t2.goto(0,-200)

t1r = 0
t2r = 0

while(True):
    text = turtle.textinput("경주게임", "파랑 or 빨강")
    if(text == "파랑" or text == "빨강"):
        break
    else:
        continue

while(t1r < 300 and t2r < 300):
    
    t1m = random.randint(1,5)
    t2m = random.randint(1,5)
    
    t1.fd(t1m)
    t2.fd(t2m)
    
    t1r += t1m
    t2r += t2m
    
    print("t1: ",t1r," vs t2: ",t2r)
    
if(t1r >= t2r):
    t1.write("승리", font=("굴림",20))
    win = "파랑"
else:
    t2.write("승리", font=("굴림",20))
    win = "빨강"
    
if(text == win):
    t.write("예측 성공")
else:
    t.write("예측 실패")

turtle.exitonclick()
turtle.bye()