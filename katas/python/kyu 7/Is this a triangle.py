#https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(a, b, c):
    if a >= b + c:
        return False
    elif b >= a + c:
        return False
    elif c >= a + b:
        return False
    else:
        return True
        