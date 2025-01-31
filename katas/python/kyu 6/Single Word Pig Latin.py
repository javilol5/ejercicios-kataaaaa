#https://www.codewars.com/kata/558878ab7591c911a4000007

def pig_latin(palabra):
    
    if not palabra:
        return None
    
    for caracter in palabra:
        if caracter.isalpha():
            continue
        else:
            return None
        
    vocales = 'aeiouAEIOU'
    
    if palabra[0] in vocales:
        return palabra.lower() + 'way'
    else:
        palabra_empieza_vocal = mover_consonantes(palabra)
        return palabra_empieza_vocal.lower() + 'ay'

def mover_consonantes(palabra):
    
    contador = 0
    while palabra[0] not in 'aeiouAEIOU' and contador <= len(palabra):
        palabra = palabra[1:] + palabra[0]
        contador += 1
    return palabra