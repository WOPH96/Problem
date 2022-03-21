
import sys
import math

k, p, n = map(int, input().split())

mod = 1000000007

x = math.ceil(math.log(p, mod))+1  # p^x > mod
for i in range(x, n+1):
    if n % i == 0:
        x = i
        break


# k * p^n % mod
# k = k* (p**n) % mod
# k = (p^x%mod)^(n/x) %mod

print(

    (k % mod * ((int(p**x) % mod) ** int((n/x))) % mod) % mod
)


# p**n % 1000000007 = 큰값
