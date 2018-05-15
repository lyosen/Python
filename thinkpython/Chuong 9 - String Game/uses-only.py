# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 23:01:09 2018

@author: tuant
"""
"""Check words was made by list_words"""


def uses_only():
    counts = 0
    words = input("Input you'r words pls:\n")
    list_words = input("Input you'r alphabet:\n")
    for i in words:
        if i in list_words:
            counts += 1
        else:
            print("%s not made by %s" % (words, list_words))
            break
    if counts == len(words):
        print("%s made by %s." % (words, list_words))
        
print(uses_only())
