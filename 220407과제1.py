# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:15:29 2022

@author: wooji
"""
import random
i = 0
t1 = 0
t2 = 0

while(1):
    t1 += random.randint(1,6)
    t2 += random.randint(1,6)
    
    print("t1: ",t1," vs t2: ",t2)
    
    if(t1 >= 30 and t2 >= 30):
        print("무승부")
        break
    elif(t1 >= 30):
        print("t1 승리")
        break
    elif(t2 >= 30):
        print("t2 승리")
        break