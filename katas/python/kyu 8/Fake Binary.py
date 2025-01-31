#https://www.codewars.com/kata/57eae65a4321032ce000002d

def fake_bin(x):
    
    result = []
    
    for digit in str(x):
        if int(digit) < 5:
            result.append('0')
        else:
            result.append('1')
    result = ''.join(result)
    return result