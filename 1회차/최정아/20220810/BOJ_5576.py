import sys
input = sys.stdin.readline

# 10개씩 나눠서 리스트 만듬
for _ in range(2):
    a = []
    for _ in range(10):
        a.append(int(input()))
    # 인덱스 -1, -2, -3가 가장 높은 수들
    # 가장 높은 수 3개의 합 출력
    print(sum(sorted(a)[-3:]), end=' ')