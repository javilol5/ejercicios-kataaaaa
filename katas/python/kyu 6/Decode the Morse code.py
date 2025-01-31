#https://www.codewars.com/kata/54b724efac3d5402db00065e

def decode_morse(morse_code):
    
    morse_code = morse_code.strip()
    
    words = morse_code.split('   ')
    
    decoded_message = []
    for word in words:
        decoded_word = ''.join(MORSE_CODE[char] for char in word.split(' '))
        decoded_message.append(decoded_word)
    
    return ' '.join(decoded_message)