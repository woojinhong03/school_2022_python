# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:57:40 2022

@author: wooji
"""

class Vect2:
    ndim = 2
    
    def __init__(self, x, y):
        self.x, self.y = x , y
        
    def __repr__(self):
        return 'Vector[' + '%.2f'%self.x + ', ' + '%.2f'%self.y + ']'
    
    def __add__(self, other):
        new = Vect2(0,0)
        new.x = self.x + other.x
        new.y = self.y + other.y
        return new
    
if __name__ == '__main__':
    v1 = Vect2(3,5)
    v2 = Vect2(7,4)
    v3 = v1 + v2
    print(v1, v2, v3)