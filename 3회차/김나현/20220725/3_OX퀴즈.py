# https://www.acmicpc.net/problem/8958
# import sys

# sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
for test_case in range(T):
    state = list(input())
    res = 0
    continuity = 1
    for i in range(len(state)):
        if (i == 0 and state[i] == 'O'):
            res += continuity
            continue
        if (state[i] == 'O' and state[i - 1] == 'O'):
            continuity += 1
            res += continuity
        else:
            if (state[i] == 'O'):
                res += 1
                continuity = 1
    print(res)