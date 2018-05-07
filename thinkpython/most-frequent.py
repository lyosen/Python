# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:18:56 2018

@author: tuant

most_frequent nhận vào một string ==> sắp xếp các ký tự theo tần xuất giảm dần
"""

def most_frequent():
    string = input("Please in put strings: \n")
    strings = string
    counts = 0
    a = []
    most_frequent_list = []
    while len(strings) > 0:
        # Đếm số lần xuất hiện của ký tự 
        counts = strings.count(strings[0])
        # thêm số lần và ký tự tương ứng vào một list
        a.append((counts, strings[0]))
        # xóa ký tự sau khi đã append - sau khi xóa, len của chuỗi xẽ giảm theo số ký tự đã xóa
        strings = strings.replace(strings[0],"")


    for i in reversed(sorted(a)):
        most_frequent_list.append(i)


    print("Số lần xuất hiện các ký tự theo thứ tự giảm dần \n trong chuỗi %s như sau: \n %s" %(string, most_frequent_list))

most_frequent()