# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:07:20 2022

@author: wooji
"""

answer = 7

while(1):
    number = int(input("정답은?:"))
    if(number > answer):
        print("정답은 더 낮은 수")
    elif(number < answer):
        print("정답은 더 높은 수")
    else:
        print ("정답입니다.")
        break