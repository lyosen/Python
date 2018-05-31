# -*- coding: utf-8 -*-
'''
 * @Author: Nguyễn Lê Tuấn - Lyosen
 * @Email: ngletuan1989@gmail.com
 * @Phone: 0996246668
 * @Date: 2018-05-31 09:03:09
 * @Last Modified by: Nguyễn Lê Tuấn - Lyosen
 * @Last Modified time: 2018-05-31 09:03:09
'''


def binarySearch(ls, number):
    """Binary Search"""
    first = 0
    last = len(ls)-1
    done = False

    while first <= last and not done:
        mid = (first+last) // 2
        if ls[mid] == number:
            done = True
        else:
            if ls[mid] > number:
                last = last-1
            else:
                first = first+1
    return done


ls = [i for i in range(0, 1000, 2)]
print(binarySearch(ls, 9999999))
