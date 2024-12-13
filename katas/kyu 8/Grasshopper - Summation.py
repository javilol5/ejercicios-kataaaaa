#https://www.codewars.com/kata/55d24f55d7dd296eb9000030

def summation(num):
    i = 0
    lista = []
    while i <= num:
        lista.append(i)
        i += 1
    return sum(lista)