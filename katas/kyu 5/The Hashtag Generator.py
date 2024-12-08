#https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    
    variable = s.split()
    result = "#"
    for loqquieras in variable: 
        result += loqquieras.capitalize()
    if result == "#" or len(result) > 140: 
        return False
    return result