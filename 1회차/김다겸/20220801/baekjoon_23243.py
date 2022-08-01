import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 가능 여부 확인
flag = True

for i in range(m):
    # 더미 갯수 입력
    length = int(input())
    # 더미 입력 받기
    stacks = list(map(int, input().split()))
    for j in range(length-1):
        # 더미의 뒤쪽 값이 더 크면
        if stacks[j] < stacks[j+1]:
            # 순차 출력 불가능
            flag = False
            break

# 순차 출력 가능하면
if flag:
    # Yes 출력
    print('Yes')
else:
    print('No')