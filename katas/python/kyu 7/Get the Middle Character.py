#https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    while len(s) > 2:
        s = s[1:-1]
    return s