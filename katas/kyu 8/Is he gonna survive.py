#https://www.codewars.com/kata/59ca8246d751df55cc00014c

def hero(bullets, dragons):
    if dragons == 0:
        return True
    return bullets // dragons >= 2