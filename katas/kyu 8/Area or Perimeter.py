#https://www.codewars.com/kata/5ab6538b379d20ad880000ab

def area_or_perimeter(l , w):
    if l == w:
        return( l * w )
    else:
        return( l + l + w + w )