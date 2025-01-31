#https://www.codewars.com/kata/5e030f77cec18900322c535d

def minimum(a, x):
    r = a % x
    if r == 0:
        return 0
    return min(r, x - r)