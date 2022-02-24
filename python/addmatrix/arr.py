def solution(arr1, arr2):
    answer = [[]]
    
    # print(arr1.size())
    #print(arr1[0][0]+arr2[0][0])
    for x,y in arr1, arr2:
        #print(x,y)
        for elm1,elm2 in x,y:
            print(elm1,end="")#,elm2)
    
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
