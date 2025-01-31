#https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])



#def spin_words(sentence):
#    
#    words = sentence.split()
#    
#    result = [word[::-1] if len(word) >= 5 else word for word in words]
#    
#    return ' '.join(result)



#def spin_words(sentence):
#    arr = sentence.split()
#    sol = []
#    
#    for char in arr:
#        if len(char) < 5:
#            sol.append(char)
#        elif len(char) >= 5:
#            back = char[::-1]
#            sol.append(back)
#    return ' '.join(sol)