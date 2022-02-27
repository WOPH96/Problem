def min(a, b):
    return a if a < b else b


def max(a, b):
    return a if a > b else b


def solution(n, m):
    answer = []

    if m % n == 0:
        return [n, m]

    elif n % m == 0:
        return [m, n]

    GCD = 0

    for gcd in reversed(range(1, min(n, m))):  # 거꾸로 하면 더 효율적
        if(n % gcd == 0 and m % gcd == 0):
            GCD = gcd
            break
    LCM = int(max(n, m)/GCD * min(n, m))
    # print(LCM)
    answer = [GCD, LCM]
    return answer


print(solution(3, 12))
print(solution(2, 5))
print(solution(300, 500))

''' 
backward
〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.4MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
테스트 12 〉	통과 (0.12ms, 10.3MB)
테스트 13 〉	통과 (0.13ms, 10.1MB)
테스트 14 〉	통과 (0.15ms, 10.1MB)
테스트 15 〉	통과 (0.04ms, 10.1MB)
테스트 16 〉	통과 (0.08ms, 10.3MB)

forward
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
테스트 12 〉	통과 (0.11ms, 10.3MB)
테스트 13 〉	통과 (0.07ms, 10.2MB)
테스트 14 〉	통과 (0.10ms, 10.2MB)
테스트 15 〉	통과 (0.05ms, 10.2MB)
테스트 16 〉	통과 (0.08ms, 10.1MB)
'''
