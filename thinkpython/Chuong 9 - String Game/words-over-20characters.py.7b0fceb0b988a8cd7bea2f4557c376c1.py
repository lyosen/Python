# -*- coding: utf-8 -*-
'''
 * @Author: Nguyễn Lê Tuấn - Lyosen
 * @Email: ngletuan1989@gmail.com
 * @Phone: 0996246668
 * @Date: 2018-05-16 15:12:58
 * @Last Modified by:   Nguyễn Lê Tuấn - Lyosen
 * @Last Modified time: 2018-05-16 15:12:58
'''


fopen = open("words.txt", "r")
fread = fopen.read()
for i in fread:
    if len(i) > 0:
        print(i)
