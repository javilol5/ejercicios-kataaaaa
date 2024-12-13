#https://www.codewars.com/kata/51c8991dee245d7ddf00000e

def reverse_words(input_string):
    words = input_string.split()
    
    reversed_words = words[::-1]
    
    return ' '.join(reversed_words)