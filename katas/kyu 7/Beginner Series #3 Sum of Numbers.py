#https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(a,b):
    suma = 0  
    
    if a <= b:
        numbers = list(range(a, b + 1))
        
    elif b < a:
        numbers = list(range(b, a + 1))

    for sol in numbers:

        suma = sol + suma              
    return(suma)