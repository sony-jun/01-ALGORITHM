# https://www.acmicpc.net/problem/3052
import sys

sys.stdin = open("1_나머지.txt")

M_list = []

for i in range(10):             # 10개 들어감
    N = int(input())
    M = N % 42
    M_list.append(M)            # 나머지를 리스트에 넣음

print(len(set(M_list)))         # set으로  중복 제거 
                                # 길이를 재면 남은 숫자 갯수