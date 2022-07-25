# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("./3회차/신윤식/20220725/0_숫자의개수.txt")

# 1.
A = int(input())    # 입력을 3번 받아야함 
B = int(input())
C = int(input())

result = str(A*B*C) # 순회를 통해 접근하는 것이 좋다고 생각하여 숫자를 문자열로 변환
lst = [0]*10  # 0~9까지 갯수 0개로 초기화

for i in result:           
    for j in range(10):   
        if i == str(j):   # j 0~9까지 순회하며 i번째 result에 있는 문자열과 같은지 확인 
            lst[j] += 1   # 만약 같다면 lst의 j번째 값 더하기 1

# for k in lst:
#     print(k)


# 2.
A = int(input())
B = int(input())
C = int(input())

T = str(A*B*C)
for i in range(10):
    print(T.count(str(i)))