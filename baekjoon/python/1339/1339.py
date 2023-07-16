import sys
from collections import deque
sys.stdin = open('1339_input.txt','r')


'''
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 
모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다.

문자의 자릿수에 해당하는 dict
ACDEB
GCF
=> 10000, 1000, 100, 10, 1
=> 100,10,1

'''

n = int(input())
words = [input() for _ in range(n)]

alpha_dict={} #자릿수 저장
nums = []
# print(words)
for word in words:
    for i,alpha in enumerate(reversed(word)) :
        if alpha in alpha_dict:
            alpha_dict[alpha]+= 10**i
        else:
            alpha_dict[alpha] = 10**i 
for num in alpha_dict.values():
    nums.append(num)
nums.sort(reverse=True)
# print(nums)
sum = 0
start = 9

for num in nums:
    sum+=num*start
    start-=1
print(sum)


