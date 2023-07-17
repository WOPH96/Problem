import sys
sys.stdin = open('14888_input.txt','r')

n = int(input())
nums = list(map(int,input().split()))
tools = list(map(int,input().split())) # + - * / 
print(n,nums,tools)

