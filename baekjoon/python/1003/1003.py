import sys
sys.stdin = open('1003_input.txt', 'r')


def sol():
    def fibo(n):
        if n == 0:
            return (1, 0)
        if n == 1:
            return (0, 1)
        if dp[n] != 0:
            return dp[n]
        dp[n] = tuple(map(lambda x, y: x+y, fibo(n-1), fibo(n-2)))
        return dp[n]
    t = int(input())
    for _ in range(t):
        dp = [0]*41
        n = int(input())

        res = fibo(n)
        print(res[0], res[1], sep=" ")


sol()
