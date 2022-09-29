# https://www.acmicpc.net/problem/15953

import sys
input = sys.stdin.readline

T = int(input())
festival1 = {
    500: 1,
    300: 2,
    200: 3,
    50: 4,
    30: 5,
    10: 6 
}
festival2 = {
    512: 1,
    256: 2,
    128: 4,
    64: 8,
    32: 16
}

for test_case in range(T):
    f1, f2 = map(int, input().split())
    result = 0

    temp = 0
    if f1 == 0:
        result += 0
    else:
        for k, v in festival1.items():
            temp += v
            if temp >= f1:
                result += k
                break
    temp = 0
    if f2 == 0:
        result += 0
    else:
        for k, v in festival2.items():
            temp += v
            if temp >= f2:
                result += k
                break
    print(result * 10000)