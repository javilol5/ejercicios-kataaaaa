#https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(arr):
    result = 0
    for num in arr:
        result ^= num
    return result