
import sys
import math

#k, p, n = map(int, input().split())
k, p, n = (100000000, 100000000, 1000000)
mod = 1000000007

x = math.ceil(math.log(p, mod))  # p^x > mod
print("first =",x)
for i in range(x, n+1):
    if n % i == 0:
        x = i
        break
print("second =",x)

# k * p^n % mod
# k = k* (p**n) % mod
# k = (p^x%mod)^(n/x) %mod

# print(int(p**x)%mod)

print(

    (k % mod * ((int(p**x) % mod) ** int((n/x))) % mod) % mod
)


# p**n % 1000000007 = 큰값
