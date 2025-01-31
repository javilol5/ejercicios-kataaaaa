#https://www.codewars.com/kata/59f11118a5e129e591000134

from collections import Counter

def repeats(arr):
    counts = Counter(arr)
    result = sum(num for num, count in counts.items() if count == 1)
    
    return result



def repeats(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    result = 0
    for num in count:
        if count[num] == 1:
            result += num

    return result



def repeats(arr):
    return sum(n for n in arr if arr.count(n) == 1)