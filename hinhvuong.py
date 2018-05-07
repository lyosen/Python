# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:14:32 2018

@author: tuant
"""

def y(n,d):
    a1 = "  "*(d-2)
    b1 = "| "
    c1 = (a1+b1) * n
    for i in range(d-2):
        print("|",c1)
def x(n,d):
    a2 = " -"*(d-2)
    b2 = " +"
    c2 = (a2 + b2) * n
    print("+"+ c2)
   
    

def hinhvuong(n,d):
    a3 = " -"*(d-2)
    b3 = " +"
    c3 = (a3 + b3) * (n)
    for i in range(n):
        x(n,d)
        y(n,d)
        print("+"+c3)
        
hinhvuong(5,8)