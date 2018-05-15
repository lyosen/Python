# -*- coding: utf-8 -*-
"""
@author: tuant
"""


def is_abecedarian():
    """ Kiem tra ky tu co theo thu tu bang chu cai khong"""
    words = input("Nhap day ky tu: \n")
    list_words = []

    for i in words:
        list_words.append(i)
    list_words_sorted = list_words[:]
    list_words_sorted.sort()

    if list_words_sorted == list_words:
        print("True")
    else:
        print("False")


is_abecedarian()
