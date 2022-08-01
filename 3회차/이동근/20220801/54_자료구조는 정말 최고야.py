import sys

N, M = map(int, sys.stdin.readline().split())

# 더미 중 순서가 하나라도 오름차순이면 불가능하다.
result = True
for _ in range(M):
    # 둘 다 sys 를 안쓰면 시간초과가 난다..
    size = int(sys.stdin.readline())
    queue = list(map(int, sys.stdin.readline().split()))

    if queue != sorted(queue, reverse=True):
        result = False
        break

print("Yes" if result else "No")