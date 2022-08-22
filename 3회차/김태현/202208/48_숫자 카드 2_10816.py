# 정수 M 리스트를 반복하며,
# 상근 리스트 내에 있으면, count 개수 저장

import sys
sys.stdin = open("48_숫자 카드 2_10816.txt", "r")

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))


N_dic = {}
for num in N_list:
    if N_dic.get(num, 0):
        N_dic[num] += 1
    else:
        N_dic[num] = 1

for num in M_list:
    if N_dic.get(num, 0):
        print(N_dic[num], end=" ")
    else:
        print(0, end=" ")