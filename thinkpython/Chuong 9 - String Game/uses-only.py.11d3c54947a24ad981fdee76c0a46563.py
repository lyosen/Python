# -*- coding: utf-8 -*-
'''
 * @Author: Nguyễn Lê Tuấn - Lyosen
 * @Email: ngletuan1989@gmail.com
 * @Phone: 0996246668
 * @Date: 2018-05-16 15:15:09
 * @Last Modified by:   Nguyễn Lê Tuấn - Lyosen
 * @Last Modified time: 2018-05-16 15:15:09
'''


def uses_only():
    counts = 0
    words = input("Input you'r words pls:\n")
    list_words = input("Input you'r alphabet:\n")
    for i in words:
        if i in list_words:
            counts += 1
        else:
            print("%s not made by %s dsadsadasdasdasdasdasdasdasdasdasdasdas " % (words, list_words))
            break
    if counts == len(words):
        print("%s made by %s." % (words, list_words))

print(uses_only())
