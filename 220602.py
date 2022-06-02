# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:04:19 2022

@author: wooji
"""

class Rect:
    count = 0
    
    def __init__(self, width, height):
        self.width, self.height = width, height
        Rect.count += 1
        self.rectid = 'rectid_' + str(Rect.count)
        
    def get_area(self):
        return (self.width * self.height)
    
    def get_peri(self):
        return 2 * (self.width + self.width)
        
if __name__ == '__main__':
    r1 = Rect(3,5)
    r2 = Rect(4,7)
    print('r1 = ', r1.width, r1.height, r1.count)
    print('r2 = ', r2.width, r2.height, r2.count)
