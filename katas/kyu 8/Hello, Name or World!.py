#https://www.codewars.com/kata/57e3f79c9cb119374600046b

def hello(name=''):
    
    name = name.capitalize()
    a = str(name)
    
    if a == '':
        nombre = 'World'
    else:
        nombre = a
    
    
    return('Hello, ' + nombre + '!')