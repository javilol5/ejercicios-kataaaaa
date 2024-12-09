#https://www.codewars.com/kata/52fb87703c1351ebd200081f

def what_century(year):
    century = (int(year)-1) // 100 + 1
    century = str(century)
    if century [0] == '1':
        century += 'th'
    elif century [-1] == '1':
        century += 'st'
    elif century [-1] == '2':
        century += 'nd'
    elif century [-1] == '3':
        century += 'rd'
    else:
        century += 'th'
    
    return(century)