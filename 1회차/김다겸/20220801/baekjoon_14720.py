import sys
input = sys.stdin.readline

n = int(input())

store = list(map(int, input().split()))

milk = 0

for i in range(n):
    # 리스트에 있는 값이 milk를 3으로 나눈 나머지이면
    if store[i] == milk % 3:
        # milk에 1 증가
        milk += 1

# milk의 합계 출력
print(milk)