def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if( i == round(i**(1/2),2)**2): # 제곱근이 있는 수라면
            i *= -1
        answer += i
    return answer