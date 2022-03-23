
import sys
import math

#k, p, n = map(int, sys.stdin.readline().split())
k, p, n = (int(1e8), int(1e8), int(1e16))
mod = 1000000007


# k = k* (p**n) % mod

result = 1

# k*(p**n) %mod =  p * p * p * p * p ... * p * k  % mod

for _ in range(n):
    result *= pimport sys

k,p,n = map(int,sys.stdin.readline().split())

# 0.1초당 P배씩 증가
# 1초당 P**10씩 증가
mod = 1000000007
res = 1

#res = k * (p **10)**n % mod


# increase per sec
ips = 1

for _ in range(10):
    ips*=p
    ips%=mod

# main

for _ in range(n):
    res*=ips
    res%=mod

res*=k
res%=mod

print(res)

    result %= mod

result *= k
result %= mod

print(result)


# p**n % 1000000007 = 큰값
 '''
 import sys

k,p,n = map(int,sys.stdin.readline().split())

# 0.1초당 P배씩 증가
# 1초당 P**10씩 증가
mod = 1000000007
res = 1

#res = k * (p **10)**n % mod


# increase per sec
ips = 1

for _ in range(10):
    ips*=p
    ips%=mod

# main

for _ in range(n):
    res*=ips
    res%=mod

res*=k
res%=mod

print(res)

 '''