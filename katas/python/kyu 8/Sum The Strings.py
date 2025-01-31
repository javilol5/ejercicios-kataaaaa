#https://www.codewars.com/kata/5966e33c4e686b508700002d

def sum_str(a, b):
    
    if a == "" and b == "":
        return '0'
    elif b == "":
        return a
    elif a == "":
        return b
    x = int(a)  
    y = int(b)
    if x == 0 and y == 0:
        return 0
    else:
        return f'{x + y}'