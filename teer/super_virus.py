
import sys
import math

#k, p, n = map(int, sys.stdin.readline().split())
k, p, n = (int(1e8), int(1e8), int(1e16))
mod = 1000000007


# k = k* (p**n) % mod

result = 1

# k*(p**n) %mod =  p * p * p * p * p ... * p * k  % mod

for _ in range(n):
    result *= p
    result %= mod

result *= k
result %= mod

print(result)


# p**n % 1000000007 = 큰값
