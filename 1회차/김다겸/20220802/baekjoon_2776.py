import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    a_n = int(input())
    # 시간 초과를 방지하기 위해 순서가 필요없는 a를 set로 입력 받기
    a = set(map(int, input().split()))
    b_n = int(input())
    b = list(map(int, input().split()))

    for i in b:
        if i in a:
            print(1)
        elif i not in a:
            print(0)