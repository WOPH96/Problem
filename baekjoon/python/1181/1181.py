import sys
sys.stdin = open('1181_input.txt', 'r')

words = set()
n = int(input())

for _ in range(n):
    words.add(input())

words = list(words)
words.sort(key=lambda x: [len(x), x])

for word in words:
    print(word)
