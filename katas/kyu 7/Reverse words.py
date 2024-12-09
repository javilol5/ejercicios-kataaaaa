#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

def reverse_words(str):
    newStr = []
    for i in str.split(' '):
            newStr.append(i[::-1])
    return ' '.join(newStr)