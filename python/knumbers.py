def k(array,command):
    i,j,k = command

    ls = array[i-1:j]
    ls.sort()
    return ls[k-1]
    
def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(k(array,command))
    return answer