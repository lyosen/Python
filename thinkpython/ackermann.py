# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:42:49 2018

@author: tuant
"""
def ack(m,n):
    """Ackermann Def"""
    if m == 0:
        return (n + 1)
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1,ack(m,n-1))

