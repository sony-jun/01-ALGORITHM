# https://www.acmicpc.net/problem/17388
import sys
sys.stdin = open('B17388.txt')
T = int(input())
for tc in range(T):
    uni = list(map(int, input().split()))
    if sum(uni) >= 100:
        print('OK')
    else:
        if min(uni) == uni[0]:
            print('Soongsil')
        elif min(uni) == uni[1]:
            print('Korea')
        else:
            print('Hanyang')