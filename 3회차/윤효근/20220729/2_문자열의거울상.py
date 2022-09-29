import sys

sys.stdin = open("0_", "r")

T = int(input())

for test_case in range(1, T + 1):
    s=list(map(ord,input()))
    for i in range(len(s)):
        if s[i] < 100:
            s[i] = chr(100)
        elif s[i] %10 ==0:
            s[i] = chr(98)
        elif s[i] == 112:
            s[i] = chr(113)
        else:
            s[i] =chr(112)
    s=''.join(s[::-1])
    print(f'#{test_case} {s}')

