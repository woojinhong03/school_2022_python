# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:07:20 2022

@author: wooji
"""

import turtle
t = turtle.Turtle()
t.shape("turtle")
ts = turtle.getscreen()

size1 = 200
size2 = 50
move_length = 10
t.dot(size1*2, "green")


while(1):
        
    d = t.distance(0,0)
     
    def key_Right():
        t.undo()
        t.dot(size1*2, "green")
        t.fd(move_length)
        print("key_Right")
        print("위치: ",t.pos())
        print("거리: ", t.distance(0,0))
        t.dot(size2*2, 'blue')
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
    
    def mclick(x,y):
        t.undo()
        t.dot(size1*2, "green")
        t.goto(x, y)
        print("click", x, y)
        print("위치: ",t.pos())
        print("거리: ", t.distance(0,0))
        t.dot(size2*2, 'blue')
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
  
    def key_exit():
        turtle.bye()
        
    ts.listen()
    ts.onkey(key_Right, "Right")
    ts.onkey(key_exit, "q")
    ts.onclick(mclick)
    ts.mainloop()


turtle.bye()