#https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    
    return '.'.join([word[0] for word in name.upper().split()])
    
    
    
#    sol = [word[0] for word in name.upper().split()]
#    return '.'.join(sol)



#    name = name.upper().split()
#    sol = [word[0] for word in name]
#    return '.'.join(sol)



#    name = name.upper()
#    name2 = name.split()
#    sol = [word[0] for word in name2]
#    return '.'.join(sol)


   
#    name = name.upper()
#    name2 = name.split()
#    sol = []
#    for word in name2:
#        sol.append(word[0])
#    return '.'.join(sol)