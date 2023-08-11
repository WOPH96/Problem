import sys
sys.stdin = open('1157_input.txt', 'r')

string = input().upper()

dic = dict()

for char in string:
    if not dic.get(char):
        dic[char] = 1
    else:
        dic[char] += 1
if len(string) == 1:
    print(string)
    exit()
M = max(dic.keys(), key=lambda k: dic[k])
v = dic[M]
dic.pop(M)

sM = max(dic.keys(), key=lambda k: dic[k])
sv = dic[sM]

if sv == v:
    print("?")
else:
    print(M)
