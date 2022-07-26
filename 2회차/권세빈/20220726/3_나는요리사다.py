# https://www.acmicpc.net/problem/2953
import sys

sys.stdin = open("3_요리사.txt", "r")

l = []                                      # 참가자들의 합산 점수를 담을 리스트
for i in range(5):                          # 다섯 참가자를 넣을 반복문
    a = sum(map(int,input().split()))       # 각 참가자들의 점수 합산
    l.append(a)                             # 리스트에 점수 담기
print(l.index(max(l))+1,max(l))             # 인덱스 함수로 위치 찾고 +1, 리스트의 최대값