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
    
    for i in list_after_cut_space:
        if "e" not in i:
            print(i)
        elif "E" not in i:
            print(i)

print(has_no_e())