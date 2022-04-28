# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:34:33 2022

@author: wooji
"""

List = ['F','B','C','A','E','D']

List = List[::-1]
print(List)
List = List[1:5]
print(List)
List = List[-2:-5:-1]
print(List)
List.reverse()
print(List)
List.append('G')
print(List)
List.sort()
print(List)