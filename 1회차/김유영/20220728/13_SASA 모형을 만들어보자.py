# https://www.acmicpc.net/problem/23825

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220728/13_SASA 모형을 만들어보자.txt")

N, M = map(int, input().split())
# 2개의 수 중에서, 가장 작은 값을 골라 내고, 가장 작은 값을 2로 나눠서 몫을 출력
SASA = min(N, M)
print(SASA//2)