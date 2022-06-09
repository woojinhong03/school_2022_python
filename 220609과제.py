# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:25:27 2022

@author: wooji
"""

import random

lottoNum = []

for i in range(6):
    while True:
        pickNum = random.randint(1, 45)
        if pickNum in lottoNum:
            continue
        else:
            lottoNum.append(pickNum)
            break

print("로또번호")
print(lottoNum)

