#https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0

def remove_char(s):
    i = list(s)
    i[0] = ''
    i[-1] = ''
    t = ''.join(i)
    return(t)