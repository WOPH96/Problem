import sys
sys.stdin = open('2910_input.txt','r')

n,c = map(int,input().split())
nums = list(map(int,input().split()))

# print(n,c,nums)

nums_dict = dict()

def freq_comp(a,b):
    pass

order=0
for num in nums:
    #한번도 등록안됐으면
    if not nums_dict.get(num):
        nums_dict[num]=[1,order]
        order+=1
    else:
        nums_dict[num][0]+=1

nums.sort(key=lambda x:(-nums_dict[x][0],nums_dict[x][1]))

for num in nums:
    print(num,end=" ")
print()
# print(nums_dict)