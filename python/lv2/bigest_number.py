from collections import deque


def func(x):
    num = deque()
    one = x % 10
    while True:
        num.appendleft(x % 10)
        if x < 10:
            break
        x //= 10
    # while(len(num) != 4): #1이었으면 *4 2였으면 *2 3이었으면 * 2 4//1 4//2 =2 4//3 = 1
    #     num.append(one)
    num = num*4
    return tuple(num)


def solution(numbers):
    answer = ''
    #numbers = [0, 0, 0, 0]
    # numbers = [3, 31, 34, 5, 0, 0, 10, 2, 1,
    #           7, 8, 593, 1234, 153, 41, 5132, 20, ]
    if(sum(numbers) == 0):
        numbers = [0]
    #numbers = [593]
    #numbers = [3, 35, 32, 5, 9]
    # func(56321)
    numbers.sort(key=func, reverse=True)
    # if 0<numbers[-1]<10 and numbers[-2]>=10:
    #     numbers[-1],numbers[-2] = numbers[-2],numbers[-1]
    # print(numbers)

    return "".join(list(map(str, numbers)))
