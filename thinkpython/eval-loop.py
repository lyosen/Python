# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:11:42 2018

@author: tuant
"""
    
def eval_loop():
    a = 0
    while True:
        string = input("")
        if (string == "huy") or (string == "Huy"):
            break
        elif len(string) == 0:
            while True:
                string = input(">: \n")
                if len(string) > 0:
                    break
        else:
            a = eval(string)
            print(a)


#a = 0
#while True:
#    string = input(">: \n")
##    print("input 1",string)
#    if string == ("huy" or "Huy"):
##        print("input 2",string)
#        break
#    elif len(string) == 0:
##        print("input 3",string)
#        while True:
#            string = input(">: \n")
##            print("input 4",string)
#            if len(string) > 0:
##                print("input 5",string)
#                break
#    else:
##        print("input 6",string)
#        a = eval(string)
#        print(a)
        