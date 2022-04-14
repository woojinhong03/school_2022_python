# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:04:34 2022

@author: wooji
"""
def bmi(k,m):
    k = k / 100
    result = m / (k*k)
    return result

while(True):
    k = int(input("키 : "))
    m = int(input("몸 : "))
    
    if(m == 0):
        break
    
    bmivalue = bmi(k,m)
    print(bmivalue)
    
