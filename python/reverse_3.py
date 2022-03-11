def solution(n):
    answer = 0
    stack = []
    while n:
        stack.append(n%3)
        n//=3

    length = len(stack)
    for i in range(length):
        answer+= stack.pop()*(3**i)
    
    return answer



# 45/3 = 15 .. 0 (1)
# 15/3 =  5 .. 0 (2)
# 5 /3 =  1 .. 2 (3)
# 1 /3 =  0 .. 1 (4)
# stack에 집어넣는다..