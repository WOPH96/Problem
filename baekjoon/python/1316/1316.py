import sys
sys.stdin = open('1316_input.txt', 'r')

n = int(input())
words = [input() for _ in range(n)]
# print(words)

cnt = 0
for word in words:
    s = []
    for char in word:
        # print(s)
        if not s:
            s.append(char)
        else:
            if s[-1] == char:
                pass
            elif char not in s:
                s.append(char)
            else:
                cnt -= 1
                break
    cnt += 1

print(cnt)
