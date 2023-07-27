from collections import deque
import sys
sys.stdin = open('1987_input.txt', 'r')

r, c = map(int, input().split())
M = max(r, c)
graph = []

for i in range(r):
    graph.append(list(input()))
for elem in graph:
    print(elem)

visited = [[[[]for _ in range(5)] for _ in range(c)]for _ in range(r)]

# 이미 들어있는지 체크 -> True면 wall이랑 똑같음


def checkin(ch):
    for i, row in enumerate(visited):
        if ch in row:
            j = row.index(ch)
            return (i, j), True
    return (0, 0), False


def bfs(G, v):
    q = deque()
    q.append((v, 0))
    visited[v[0]][v[1]][0].extend(G[v[0]][v[1]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    while q:
        cnt += 1
        (x, y), floor = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 틀에 박지 않았을때만 실행
            if 0 <= nx < r and 0 <= ny < c:
                # 이전 히스토리에 있으면 pass
                if G[nx][ny] in visited[x][y][floor]:
                    continue
                # 현재 루틴이 이미 방문 했던 문자가 아니라면
                # and G[nx][ny] not in visited[x][y]:
                if not visited[nx][ny][floor]:
                    visited[nx][ny][floor].extend(visited[x][y])
                    visited[nx][ny][floor].extend(G[nx][ny])
                    q.append(((nx, ny), floor))
                    print(nx, ny, floor, visited[x][y][floor])
                # 다른 그룹이 방문했던 흔적이 보인다면
                elif visited[nx][ny][floor][:-1] != visited[x][y][floor]:
                    visited[nx][ny][floor+1].extend(visited[x][y][floor])
                    visited[nx][ny][floor+1].extend(G[nx][ny])
                    q.append(((nx, ny), floor+1))

                '''
                (xx, yy), check = checkin(G[nx][ny])
                # 현재 루틴이 이미 방문 했던 문자가 아니라면
                if not check and visited[nx][ny] == 0:
                    visited[nx][ny] = G[nx][ny]
                    q.append((nx, ny))

                # 방문은 안했지만 이미 있던 문자
                elif check and visited[nx][ny] == 0:
                    visited[xx][yy] = 1
                    visited[nx][ny] = G[nx][ny]
                    q.append((nx, ny))
                '''
        if cnt > 1:
            break
    pass


bfs(graph, (0, 0))
# for elem in visited[:][:]:
#     print(elem)
# print(visited[0].count(isinstance(str)))
