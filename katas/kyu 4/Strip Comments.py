#https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def strip_comments(string, markers):
    lines = string.split("\n")
    list = []

    for word in lines:
        for exclamacion_hashtag in markers:
            if exclamacion_hashtag in word:
                word = word.split(exclamacion_hashtag)[0]
                
        list.append(word.rstrip())

    return "\n".join(list)