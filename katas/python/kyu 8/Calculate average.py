#https://www.codewars.com/kata/57a2013acf1fa5bfc4000921

def find_average(numbers):
    if numbers == []:
        return 0
    else:
        media = len(numbers)
        total = sum(numbers)
        return total / media