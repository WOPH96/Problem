from itertools import combinations


def solution(numbers):
    
    sums = set()
    for i in combinations(numbers,2):
        sums.add(i[0]+i[1])
    return sorted(list(sums))

print(solution([2,1,3,4,1]))