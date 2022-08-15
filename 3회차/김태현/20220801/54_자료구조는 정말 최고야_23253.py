import sys
sys.stdin = open("54_자료구조는 정말 최고야_23253.txt", "r")

# 구글링: 각 리스트가 내림차순인지 판단하는 문제

N, M = map(int, input().split())
check = bool

for i in range(M): # 더미 개수만큼
    M_len = int(input())
    M_lst = list(map(int, input().split()))
    for j in range(M_len): # 0, 1
        if M_lst[j] < M_lst[j+1]: # 내림차순 X -> No
            print("No")
            exit(0)
print("Yes")