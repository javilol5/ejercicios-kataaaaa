#https://www.codewars.com/kata/576b93db1129fcf2200001e6

def sum_array(arr):
    if arr == None:
        return 0
    arr = list(arr)
    arr.sort()
    arr = arr[1:-1]
    sum = 0
    for num in arr:
        sum = sum + num
    
    return sum