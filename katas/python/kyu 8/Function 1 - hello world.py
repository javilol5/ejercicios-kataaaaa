#https://www.codewars.com/kata/523b4ff7adca849afe000035

def greet():
    
    ascii_codes = [ 104, 101, 108, 108, 111, 32, 119 ,111, 114, 108, 100, 33]
    letters = [chr(code) for code in ascii_codes]
    result = ''.join(letters)
    
    return result