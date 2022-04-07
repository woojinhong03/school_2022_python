# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:34:21 2022

@author: wooji
"""

import random

select_com = random.choice(["가위","바위","보"])

a = input("가위, 바위, 보?:")
print("COM: ",select_com)
if(select_com == "가위" and a == "가위" or select_com == "바위" and a == "바위" or select_com == "보" and a == "보"):
    print("draw")
elif(select_com == "가위" and a == "바위" or select_com == "바위" and a == "보" or select_com == "보" and a == "가위"):
    print("win")
elif(select_com == "가위" and a == "보" or select_com == "바위" and a == "가위" or select_com == "보" and a == "바위"):
    print("lose")
else:
    print("에러")