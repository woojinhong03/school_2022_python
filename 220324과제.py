# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:40:23 2022

@author: wooji
"""
while(1):
    year = int(input("year: "))
    
    if (year % 4 == 0):
        if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
            print(year," 년은 윤년입니다")
        elif (year % 4 == 0 and year % 100 == 0):
            print(year," 년은 평년입니다")
        else:
            print(year," 년은 윤년입니다")
    else:
        print(year," 년은 평년입니다")