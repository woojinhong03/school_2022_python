# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:29:55 2022

@author: wooji
"""

age = int(input("나이 : "))
if(age <= 20):
    price = 5000
else:
    price = 10000

money_total = 0

while True:
    money = int(input("돈 : "))
    money_total = money_total + money
    if(money_total >= price):
        print(">>>거스름돈 : ", money_total - price)
        print(">>입장가능")
        break;
    else:
        print(">>추가필요금액 : ", price - money_total)
        print(">>입장불가")
        
        