# - *- coding: utf- 8 - *- .
def uses_only():
    word = input("Nhap mot tu bat ky: \n")
    string = input("Nhap mot chuoi cac chu cai: \n")
    list_word = []

    for words in word:
        if words not in string:
            list_word.append(words)

    if list_word != []:
        print("False")
    elif list_word == []:
        print("True")
uses_only()
