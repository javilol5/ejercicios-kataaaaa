#https://www.codewars.com/kata/5875b200d520904a04000003

def enough(cap, on, wait):
    if cap >= ( on + wait):
        return(0)
    else:
        return(abs(on+wait)-cap)