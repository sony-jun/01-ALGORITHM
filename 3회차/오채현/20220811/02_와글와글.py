import sys
sys.stdin = open('02_input.txt')

s, k, h = map(int, input().split())

if (s + k + h) >= 100:
    print('OK')
else:
    m = min(s, k, h)
    # if s < k and s < h:
    if s == m:
        print('Soongsil')
    elif k < s and k < h:
        print('Korea')
    elif h < s and h < k:
        print('Hanyang')
