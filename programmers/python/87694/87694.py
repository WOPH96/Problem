import sys
sys.stdin = open('87694_input.txt','r')

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    xmax=0
    ymax=0
    def make_load(G,p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        sx,bx = min(x1,x2),max(x1,x2)
        sy,by = min(y1,y2),max(y1,y2)
        for i in range()
        pass

    for (x1,y1,x2,y2) in rectangle:
        xmax = max(xmax,x1,x2)
        ymax = max(ymax,y1,y2)
        print(x1,y1,x2,y2)
    print(xmax,ymax)
    graph = [[0 for i in range(xmax+1)]for _ in range(ymax+1)]
    for elem in graph:
        print(elem)
    return answer

# print (solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],	1,	3,	7,	8)) #17
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]	,9	,7	,6	,1)) #11
print(solution([[1,1,5,7]]	,1	,1	,4	,7 ))# 9
# print(solution([[2,1,7,5],[6,4,10,10]]	,3	,1	,7	,10) )# 15
# print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]]	,1	,4	,6	,3 ))# 10