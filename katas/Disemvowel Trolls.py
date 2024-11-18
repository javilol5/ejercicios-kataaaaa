#https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")