#https://www.codewars.com/kata/52ec24228a515e620b0005ef

def exp_sum(n):
    if n < 0:
        return 0
    partitions = [0] * (n + 1)
    partitions[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    
    return partitions[n]