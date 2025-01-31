#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    return ''.join([')'if word.lower().count(char)  > 1 else '(' for char in word.lower()])



#def duplicate_encode(word):
#
#    word_toRet = ''
#    for char in word:
#        if word.lower().count(char)  > 1:
#            word_toRet += ')'
#        else:
#            word_toRet += '('
#    return word_toRet



#def duplicate_encode(word):
#
#    word = word.lower()
#    word_toRet = ''
#    for char in word:
#        if word.count(char)  > 1:
#            word_toRet += ')'
#        else:
#            word_toRet += '('
#    return word_toRet