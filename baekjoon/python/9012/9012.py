import sys
sys.stdin = open('9012_input.txt', 'r')

t = int(input())

for _ in range(t):
    # (())())
    string = input()
    # print(string)
    s = []
    Flag = False
    for elem in string:
        # print(s)
        if not s:
            if elem == ")":
                print("NO")
                Flag = True
                break
            else:
                s.append(elem)
        else:
            if elem == ")":
                out = s.pop()
                if out == ")":
                    print("NO")
                    Flag = True
                    break
            else:
                s.append(elem)
    if Flag:
        continue
    if not s:
        print("YES")
    else:
        print("NO")
