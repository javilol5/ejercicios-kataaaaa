#https://www.codewars.com/kata/554e4a2f232cdd87d9000038

def DNA_strand(dna):
    respuesta = []
    for char in dna:
        if char == 'A':
            respuesta.append('T')
        elif char == 'T':
            respuesta.append('A')
        elif char == 'G':
            respuesta.append('C')
        elif char == 'C':
            respuesta.append('G')
    return ''.join(respuesta)