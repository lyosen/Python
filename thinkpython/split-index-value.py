

def dictrandom(string):
    import random
    number = []
    for i in range(len(string)):
        number.append(random.choice(range(len(string))))
    b = dict(zip(string, number))
    return b
dictrandom("lyosen")