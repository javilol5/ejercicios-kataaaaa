#https://www.codewars.com/kata/58ae6ae22c3aaafc58000079

def permute_a_palindrome (input):
    oddCharacter = ""
    for character in input:
        occurrence = input.count(character)
        if not oddCharacter and occurrence % 2 != 0:
            oddCharacter = character
        elif oddCharacter == character:
            continue
        elif occurrence % 2 != 0:
            return False
        else:
            continue
    return True