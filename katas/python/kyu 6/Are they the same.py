#https://www.codewars.com/kata/550498447451fbbd7600041c

def comp(array1, array2):
    print(array1)
    print(array2)
    # your code
    if array1 == [] and array2 == []:
        return True
    if array2 == None or array1 == None or not array1:
        return False
    for i in array1:
        if i ** 2 not in array2:
            return False
        del array2[array2.index(i ** 2)]
    return True