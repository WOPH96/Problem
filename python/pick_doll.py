from collections import deque



def solution(board, moves):
    answer = 0
    basket=[] # stack
    moves.reverse()
    #moves = deque(moves) # queue

    
    tf = list(map(list, zip(*board)))
    
    
    # print("original=")
    # for i in board:
    #     print(i)
    # print("transform=")
    # for i in tf:
    #     print(i)
    
    remove_set={0}

    for i in range(len(tf)):
        tf[i] = [j for j in tf[i] if j not in remove_set]
    
    while moves:
        move = moves.pop()
        
        if tf[move-1]:
            doll = tf[move-1].pop(0)
            if basket:
                if doll == basket[-1]:
                    basket.pop()
                    answer+=2
                else : 
                    basket.append(doll)
            else:
                basket.append(doll)
        
        # print(basket,answer)
    
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))