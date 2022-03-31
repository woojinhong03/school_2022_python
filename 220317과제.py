# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:03:36 2022

@author: wooji
"""

don = int(input("투입한 돈 입력 : "))
pri = int(input("가격 : "))
nam = don-pri

print("거스름돈 : ", nam)

print("500원짜리 동전 ", (nam // 500) , "개")
print("100원짜리 동전 ", (nam % 500 // 100) , "개")