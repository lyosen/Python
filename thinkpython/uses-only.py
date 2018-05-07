# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 23:01:09 2018

@author: tuant
"""
"""Check words was made by list_words"""


def uses_only():
    words = (input("Input you'r words pls:\n"))
    list_words = (input("Input you'r alphabet:\n"))
    if words in list_words:
        print("%s made by %s" % (words, list_words))
    else:
        print("%s not made by %s" % (words, list_words))
