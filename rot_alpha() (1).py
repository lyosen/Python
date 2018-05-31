def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

rot_alpha(13)('Hello World')



def decrypt(encoded):
    ref = ord('r')
    clear = ord('e')
 
    a_ord = ord('a')
 
    outb = ""
 
    for c in encoded:
        oc = ord(c)
 
        # Only decrypt the alpha.
        if oc in range(ord('a'), ord('z') + 1):
            rc = chr((ord(c) - a_ord + clear - ref) % 26 + a_ord)
        else:
            rc = c
        outb += rc
    return outb
