#https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

def count_sheep(n):
    sol = ""
    for i in range(1, n + 1):
        sol += f"{i} sheep..."
    return sol