# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 09:01:33 2018

@author: tuant
"""
import time

def giaithua_for(n):
    t1 = time.time()
    giaithua = 1
    for i in range(n,0,-1):
        giaithua *= i
    t2 = time.time() - t1
    return giaithua, t2
    
    
def giaithua(n):
    if n == 0:
        return 1
    else:
        recurse = giaithua(n-1)
        ketqua = n * recurse
        return ketqua
    
    
    

    