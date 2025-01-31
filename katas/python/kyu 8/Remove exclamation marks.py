#https://www.codewars.com/kata/57a0885cbb9944e24c00008e

def remove_exclamation_marks(s):
    s = list(s)
    s = [char for char in s if char != '!']
    s = ''.join(s)
    return(s)