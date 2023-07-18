from itertools import combinations
import sys
sys.stdin = open('14889_input.txt', 'r')

n = int(input())

abilities = [list(map(int, input().split())) for _ in range(n)]

# print(abilities)

'''
N명중 N/2명 골라서 조합
6명중 3명


'''
m = 1000
people = [i for i in range(n)]
TeamLink = [0]*int(n/2)
TeamStart = [0]*int(n/2)
for TeamStart in combinations(people, int(n/2)):
    TeamLink = [x for x in people if x not in TeamStart]
    # ScoreofTeam X
    SL = SS = 0
    for a, b in combinations(TeamStart, 2):
        SS += abilities[a][b] + abilities[b][a]
    for a, b in combinations(TeamLink, 2):
        SL += abilities[a][b] + abilities[b][a]
    gap = abs(SS-SL)
    m = min(m, gap)
print(m)
#     Teamstart = abilities[a][b] + abilities[b][a]
#     Teamlink = abilities[c][d] + abilities[d][c]
#     gap = abs(Teamstart-Teamlink)
#     m = min(m, gap)
# print(m)
