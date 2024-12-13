#https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def open_or_senior(members):
    categories = []  
    for member in members:  
        age, handicap = member  
        if age >= 55 and handicap > 7:  
            categories.append("Senior")
        else:  
            categories.append("Open")
    return categories  