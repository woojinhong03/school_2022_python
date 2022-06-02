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
    r1 = Rect(3, 5)
    r2 = Rect(4, 7)
    r3 = Rect(6, 9)
    print(Rect.count, r1.count, r1.rectid)
    print(Rect.count, r2.count, r2.rectid)
    print(Rect.count, r3.count, r3.rectid)