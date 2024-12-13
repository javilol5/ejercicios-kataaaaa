#https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    snum = str(num)
    listilla = list(snum)
    sol = []
    
    for n in listilla:
        n = int(n)
        
        n = n ** 2
        sol.append(str(n))
    
    return int("".join(sol))