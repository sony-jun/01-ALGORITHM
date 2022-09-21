import sys
sys.stdin = open('54_자료구조최고야_23253.txt' ,'r')
input = sys.stdin.readline

# 각 스택이 오름차순으로 쌓여야 성공
# 스택을 입력 받고
# 하나씩 꺼내면서 오름차순인지 확인

# N: 교과서 개수, M: 묶음 수
N, M = map(int, input().split())

# 성공 / 실패
isBool = True

for i in range(M):
    # 한 더미씩 입력 받음
    num = int(input())
    num_list = list(map(int, input().split()))
    # 더미 내부 반복
    for j in range(num - 1):
        if num_list[j] < num_list[j+1]:
            isBool = False
            break
    if not isBool:
        break

print("Yes" if isBool else "No")
