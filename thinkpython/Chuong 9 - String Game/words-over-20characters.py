'''
# -*- coding: utf-8 -*- 
* @Author: Lyosen 
 * @Date: 2018-05-15 11:23:35 
 * @Last Modified by:   Nguyễn Lê Tuấn - Lyosen 
 * @Last Modified time: 2018-05-15 11:23:35 
 '''
fopen = open("words.txt", "r")
fread = fopen.read()
for i in fread:
    if len(i) > 0:
        print(i)

