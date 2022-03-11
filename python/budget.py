# greedy 사용
# 최대한 많은 부서에 지원해야하므로
# 가장 적게 요구한 부서부터 지원한다.
def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    while d:
        budget-= d.pop()
        if budget<0 : break
        answer +=1
        
    return answer