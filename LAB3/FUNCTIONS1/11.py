def IS_palin(s):
    s = s.lower()
    t = ""
    for i in s:
        t = i + t
    if (t == s):
        return True
    else:
        return False
#print(IS_palin("aka aka"))