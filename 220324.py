# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:40:23 2022

@author: wooji
"""

age = int(input("나이: "))
mon = int(input("돈: "))

if(age < 20):
    if(mon >= 5000):
        print("입장가능")
        print("거스름돈 : ", mon - 5000)
    else:
        print("입장불가")
        print("추가필요금액 : ", 5000 - mon)
else:
    if(mon >= 10000):
        print("입장가능")
        print("거스름돈 : ", mon - 10000)
    else:
        print("입장불가")
        print("추가필요금액 : ", 10000 - mon)