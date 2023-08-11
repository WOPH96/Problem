import sys
sys.stdin = open('10809_input.txt', 'r')

string = input()

for i in range(26):
    ch = chr(i+97)
    print(string.find(ch), end=" ")
    # if ch in string:
    #     print(string.index(ch), end=" ")
    # else:
    #     print(-1, end=" ")
print()
