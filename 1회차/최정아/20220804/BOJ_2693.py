
# 배열 A가 주어졌을 때, N번째 큰 값

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    # sorted 통해서 정렬
    # 7번째 index 출력
    print(sorted(list(map(int, input().split())))[7])