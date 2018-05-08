"""Has-no-e"""


def has_no_e():
    link = input("Input link of file: \n")
    fopen = open(link, "r")
    fread = (fopen.read()).strip()
    fread += " "
    count_e = 0
    count_not_e = 0
    list_no_e = []
    words = ""
    list_after_cut_space = []

    # Cut Space
    for i in fread:
        if i != " ":
            print("... not space: ",i)
            words += i
            print("..... words no space: ", words)
        else:
            list_after_cut_space.append(words)
            words = ""
    print("List after cut space: %s \nAnd len of List: %s" %(list_after_cut_space,len(list_after_cut_space)))
    
    # count no "e" and has "e"

    #  case 1 : len(list_after_cut_space) = 1 ex: list_after_cut_space = ["NguyenLETuan"]
    #  and list_after_cut_space[0] = NguyenLEtuan
    if len(list_after_cut_space) == 1:
        if len(list_after_cut_space[0]) == 0:
            return 0
        else:
            count_e += list_after_cut_space[0].count("e") 
            count_e += list_after_cut_space[0].count("E")
            percent_e = count_e * 100/(len(list_after_cut_space[0]))
            return percent_e, list_after_cut_space
    #   case 2 : len(list_after_cut_space) > 1 ex: list_after_cut_space = ["NguyenLETuan","Lyosen"]
    elif len(list_after_cut_space) > 1:
        for j in list_after_cut_space:
            if "e" not in j and "E" not in j:
                list_no_e.append(j)
                count_not_e += len(j)
                print(".. count not e: ",count_not_e)
            else:
                count_e += j.count("e")
                count_e += j.count("E")
                print (".... count e: ", count_e)
        percent_e = count_e * 100/(count_e + count_not_e)
        return percent_e, list_no_e
    # print (list_no_e,percent_e)
print(has_no_e())