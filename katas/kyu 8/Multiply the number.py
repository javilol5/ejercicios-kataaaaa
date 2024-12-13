#https://www.codewars.com/kata/5708f682c69b48047b000e07

def multiply(n):
    if n >= 0:
        long = len(str(n))
        x = 5**long
        return n*x
    elif n < 0:
        long = len(str(n)) -1
        x = 5**long
        return n*x