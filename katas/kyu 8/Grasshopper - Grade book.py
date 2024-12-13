#https://www.codewars.com/kata/55cbd4ba903825f7970000f5

def get_grade(s1, s2, s3):
    
    average = (s1 + s2 + s3)/3
    
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'