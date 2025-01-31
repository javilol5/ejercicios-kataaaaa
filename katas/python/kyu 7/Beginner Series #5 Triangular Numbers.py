#https://www.codewars.com/kata/56d0a591c6c8b466ca00118b

def is_triangular(t):
    n = 0
    
    while n < t:
    
        n = n + 1
    
    
        if t == ( n * (n + 1) / 2 ):
    
            return True
    
    return False