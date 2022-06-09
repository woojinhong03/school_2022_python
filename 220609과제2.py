# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:32:57 2022

@author: wooji
"""

poet = """ 죽는 날까지 하늘을 우러러
한 점 부끄럼이 없기를,
잎새에 이는 바람에도
나는 괴로워했다. 
별을 노래하는 마음으로 
모든 죽어가는 것을 사랑해야지
그리고 나에게 주어진 길을
걸어가야겠다.
"""


Dic = {}

for ch in poet:
    if ch in Dic:
        Dic[ch] = Dic[ch] + 1
    else:
        Dic[ch] = 1
        
del(Dic[" "])
del(Dic["\n"])

print(Dic)