import sys
sys.stdin = open('11718_input.txt', 'r')

while True:
    try:
        string = input()
        print(string)
    except Exception:
        break
