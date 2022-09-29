import sys
sys.stdin = open('06_input.txt')

f = 0

a, b, c = map(int, input().split())

tlog = [list(map(int, input().split())) for _ in range(3)]
last = max(tlog[0][1], tlog[1][1], tlog[2][1])
# 나간 시간 중 최대값 구하기

pk = [0] * (last - 1)

for t in tlog:
    # 각각의 트럭이 들어온 시간부터 나간 시간 까지의 범위에서 트럭 수 추가
    # 인덱스와 맞추기 위해 -1 해줌
    for i in range(t[0] - 1, t[1] - 1):
        pk[i] += 1

for p in pk:
    if p == 1:
        f += a
    elif p == 2:
        f += 2 * b
    elif p == 3:
        f += 3 * c
print(f)

print(pk)
