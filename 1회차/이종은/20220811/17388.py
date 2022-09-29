# 참여도가 가장 낮은 대학의 동아리 => 영어 철자 출력 

import sys 
sys.stdin = open('input1.txt')

s, k, h = map(int, input().split())

if s + k + h >= 100:
    print("OK")
else:
    if min(s, k, h) == s:
        print("Soongsil")
    elif min(s, k, h) == k:
        print("Korea")
    else:
        print("Hanyang")

