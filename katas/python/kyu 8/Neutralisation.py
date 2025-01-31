#https://www.codewars.com/kata/65128732b5aff40032a3d8f0

def neutralise(s1, s2):
    sol = ''
    for i in range(len(s1)):
        
    
        if s1[i] == s2[i]:
            sol += (s1[i])
        else:
            sol += str(0)
    
    return sol