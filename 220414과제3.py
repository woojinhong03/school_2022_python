# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:51:01 2022

@author: wooji
"""

name = []
height = []
weight = []
age = []

bts = ["슈가", 174, 57,
       "지민", 173, 53,
       "제이홉", 177, 59,
       "진", 179, 61,
       "뷔", 180, 60,
       "정국", 178, 65,
       "RM", 181, 70]

def bts_sort(bts, a):
    if (a == "name"):
        for i in range(0,21,3):
            name.append(bts[i])
        return name
    elif (a == "height"):
        for i in range(1,21,3):
            height.append(bts[i])
        return height
    elif (a == "weight"):
        for i in range(2,21,3):
            weight.append(bts[i])
        return weight
    else:
        return 
            
            
        
bts_name = bts_sort(bts, "name")
print("bts_name:", bts_name)
bts_height = bts_sort(bts, "height")
print("bts_height:", bts_height)
bts_weight = bts_sort(bts, "weight")
print("bts_weight:", bts_weight)
bts_age = bts_sort(bts, "age")
print("bts_age:", bts_age)