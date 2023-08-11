import sys
sys.stdin = open('2941_input.txt', 'r')

# string = input()

# state = ''
# cnt = 0
# for elem in string:
#     if state == '':
#         if elem == 'c':
#             state = 'c'
#         elif elem == 'd':
#             state = 'd'
#         elif elem == 'l':
#             state = 'l'
#         elif elem == 'n':
#             state = 'n'
#         elif elem == 's':
#             state = 's'
#         elif elem == 'z':
#             state = 'z'
#         else:
#             cnt += 1
#     elif state == 'c':
#         if elem == '=':
#             cnt += 1
#             state = ''
#         elif elem == "-":
#             cnt += 1
#             state = ''
#         else:
#             state = ''
#     elif state == 'd':
#         if elem == "z":
#             state = 'z'
#         elif elem == "-":
#             cnt += 1
#             state = ''
#         else:
#             cnt += 1
#             state = ''
#     elif state == 'l':
#         if elem == "j":
#             cnt += 1
#         state = ''

#     elif state == 'n':
#         if elem == "j":
#             cnt += 1
#         state = ''
#     elif state == 's':
#         if elem == "=":
#             cnt += 1
#         state = ''
#     elif state == 'z':
#         if elem == "=":
#             cnt += 1
#         state = ''

#     print(state, cnt)
# print(cnt)
