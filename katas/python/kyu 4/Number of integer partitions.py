#https://www.codewars.com/kata/546d5028ddbcbd4b8d001254

def partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            dp[i] += dp[i - k]
    
    return dp[n]