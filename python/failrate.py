def solution(N, stages):
    answer = []
    stages.sort(reverse=True)
    group =[]
    while stages:
        #print(stages)
        clger = len(stages) # 8
        stage = stages.pop() # 1
        if stage == N+1 :
            break
        cnt = 1
        
        for i in stages[::-1]:
            if i == stage:
                cnt+=1
            else : break
        #print(cnt)
        stages = stages[:1-cnt] if cnt > 1 else stages
        # if stage == N+1 : 
        #     cnt = 0
        #     stage =N
        group.append((stage,cnt/clger))
    
    counted = list(map(lambda x:x[0],group))
    for i in range(1,N+1):
        if i not in counted:
            group.append((i,0.0))
    answer = list(map(lambda x: x[0],sorted(group,key=lambda x : (-x[1],x[0]))))
    print(group)
    return answer
