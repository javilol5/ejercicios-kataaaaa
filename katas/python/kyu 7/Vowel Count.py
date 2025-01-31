#https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    vocales = 'aeiou'
    vocal = 0
    sentence = sentence.lower()
    for char in vocales:
        vocal += sentence.count(char)
        
    return vocal