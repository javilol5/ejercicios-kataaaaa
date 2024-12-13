#https://www.codewars.com/kata/5583090cbe83f4fd8c000051

def digitize(n):
    return [int(num) for num in str(n)][::-1]