import sys
sys.stdin = open('2775_input.txt', 'r')


def sol():
    def people(k, n):
        if k == 0:
            dp[k][n] = n
            return n
        if dp[k][n] != 0:
            return dp[k][n]
        for i in range(1, n+1):
            dp[k][n] += people(k-1, i)
        return dp[k][n]
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

        print(people(k, n))
        # print(dp)


sol()
