#https://www.codewars.com/kata/5412509bd436bd33920011bc

def maskify(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]