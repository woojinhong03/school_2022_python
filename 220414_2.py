# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:29:05 2022

@author: wooji
"""

import random

num = [0,0,0,0,0,0,0,0,0,0]

for i in range (100):
    num_int = random.randint(0, 9)
    num[num_int] = num[num_int] + 1
    

print(num)