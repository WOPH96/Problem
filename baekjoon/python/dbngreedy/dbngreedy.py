import sys
sys.stdin = open('dbngreedy_input.txt', 'r')

S = input()
sum = 0
lst = []
isexist = False
for elem in S:
    if elem.isalpha():
        lst.append(elem)
    else:
        sum += int(elem)
        isexist = True

lst.sort()

if isexist:
    lst.append(str(sum))

print("".join(lst))
