"""Has-no-e"""


def has_no_e(link):
    f = open(link,"r")
    count_e = 0
    count_not_e = 0
    list_no_e = []
    for i in f:
        for j in i:
            if "e" not in j:
                list_no_e.append(j)
                count_not_e += 1
            else:
                count_e += 1
    percent_e = count_e * 100/(count_not_e + count_e)
    return percent_e, list_no_e


