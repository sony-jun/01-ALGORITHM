# https://www.acmicpc.net/problem/2309
from os import remove
import sys

sys.stdin = open("1_일곱 난쟁이.txt")


N_list = []
sum_list = []

for _ in range(9):
    N_list.append(int(input()))                             # 9명의 키 추가

sum_list = sum(N_list)                                      # 9명의 키 더하기

for i in range(8):                                          
    for j in range(i+1, 9):
        if sum_list - (N_list[i] + N_list[j]) == 100:       # 9명의 총 합에서 2명을 빼면 100이 되는 인덱스 찾기
            N1 ,N2 = N_list[i], N_list[j]                   # 맞으면 N1과 N2에 값 추가

            N_list.remove(N1)                               # 첫번째 가짜 난쟁이 제거
            N_list.remove(N2)                               # 두번째 가짜 난쟁이 제거
            break

    if len(N_list) == 7:                                    # 두명이 제거 되면 7명
        break

N_list.sort()                                               # 정렬

for i in range(7):
    print(N_list[i])
