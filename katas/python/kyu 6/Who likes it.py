#https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    long = len(names)
    longmenos = long-2
    if long == 0:
        return 'no one likes this'
    elif long == 1:
        return names[0] + ' likes this'
    elif long == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    elif long ==3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        return names[0] + ', ' + names[1] + ' and ' + str(longmenos) + ' others like this'