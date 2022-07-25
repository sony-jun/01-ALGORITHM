# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("/Users/mac/Desktop/TIL/01-ALGORITHM/2회차/최준혁/20220725/0_숫자의개수.txt")

A, B, C = map(int, sys.stdin.readlines())
multi_list = list(map(int, str(A*B*C)))
cnt = 0
cnt_list = []

for i in range(10): # 0~9까지
    for j in range(len(multi_list)): # multi_list의 길이 만큼
        if multi_list[j] == i: # 리스트 내의 값이 i와 같으면
            cnt += 1 # 카운트를 늘리고
    cnt_list.append(cnt) # 카운트 리스트에 추가 
    cnt = 0 # 초기화 

for i in range(len(cnt_list)): # 리스트의 길이 동안
    print(cnt_list[i]) # 리스트 내의 값 출력 

sys.stdin.close