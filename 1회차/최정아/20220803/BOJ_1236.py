# 몇 명의 경비원을 최소로 추가

# 성의 세로 크기: N, 가로 크기: M 주어짐
n, m = map(int, input().split())
# 성의 빈 리스트 생성
castle = []


for i in range(n):
    castle.append(input())

a, b = 0, 0

for i in range(n):
    # 경비원이 있는 칸 X가 i에 없으면
    if "X" not in castle[i]:
        # a에 1씩 증가
        a += 1

for j in range(m):
    if "X" not in [castle[i][j] for i in range(n)]:
        b += 1
# 경비원의 최솟값 출력
print(max(a, b))