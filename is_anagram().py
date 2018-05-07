def is_anagram():
    anagram = input("Nhap mot tu bat ky: \n")
    new_anagram = anagram[::-1]
    if new_anagram == anagram:
        print("True")
    else:
        print("False")
is_anagram()

