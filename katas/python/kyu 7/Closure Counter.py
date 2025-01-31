#https://www.codewars.com/kata/60edafd71dad1800563cf933

def counter():
    count = 0
    def function():
        nonlocal count
        count += 1
        return count
    return function