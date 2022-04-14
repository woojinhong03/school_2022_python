# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:31:07 2022

@author: wooji
"""

import turtle

def don(mon,nara):
    if nara == "미국":
        return (mon / 1117.5)
    elif nara == "일본":
        return (mon / 1022.56)
    elif nara == "유럽연합":
        return (mon / 1343.24)
    else:
        print("잘못된 국가 연합입니다.")
        return 0
    
while(1):
    mon = float(turtle.textinput("환전계산","KRW"))
    nara = turtle.textinput("환전계산", "국가")
    
    if(mon == 0):
        break
    
    a = don(mon,nara)
    print(a)