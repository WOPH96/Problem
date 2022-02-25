from math import *

def is_square_root(n):

    return n==pow(round(sqrt(n)),2)

def solution(n):
    
    #print(is_square_root(n))
    
    if is_square_root(n):
        return int(pow(sqrt(n)+1,2))

    else :
        return -1


print(solution(121))