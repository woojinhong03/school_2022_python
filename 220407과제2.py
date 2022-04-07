# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:26:50 2022

@author: wooji
"""

import turtle
import random

text = turtle.textinput("주사위게임", "t1 or t2")


t1 = 0
t2 = 0

while(1):
    t1 += random.randint(1,6)
    t2 += random.randint(1,6)
    
    print("t1: ",t1," vs t2: ",t2)
    
    if(t1 >= 30 and t2 >= 30):
        print("무승부")
        a = "무승부"
        break
    elif(t1 >= 30):
        print("t1 승리")
        a = "t1"
        break
    elif(t2 >= 30):
        print("t2 승리")
        a = "t2"
        break

if(text == a):
    print("맞췄습니다.")
else:
    print("틀렸습니다.")