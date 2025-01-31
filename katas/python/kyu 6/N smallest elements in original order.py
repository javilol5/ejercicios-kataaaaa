#N smallest elements in original order

def first_n_smallest(arr, n):
    if n == 0: return []
    reversed_array = arr[::-1]
    
    while len(reversed_array) != n:
        reversed_array.pop(reversed_array.index(max(reversed_array)))
    return reversed_array[::-1]



#def first_n_smallest(arr, n):
#    lst = sorted(enumerate(arr), key=lambda it: it[1])[:n]
#    lst.sort(key=lambda it:it[0])
#    return [v for _,v in lst]



#def first_n_smallest(arr, n):
#    m = sorted(arr)[:n]
#    return [m.pop(m.index(i)) for i in arr if i in m]