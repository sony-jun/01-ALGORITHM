# import sys
# sys.stdin = open('박스_input.txt')

# m이 행, n이 열
# 열은 고정
# 행으로 이동

# T = int(input())

m, n = map(int, input().split())
box = []

ans = [0] * T
# for t in range(T):
for _ in range(m):
    box.append(list(input().split()))

# 열행 box 
# 10101
# 00010
# 01001
# 00100
# 자기 위치(열) - 박스 수(열)
# 첫 번째에 1이 3개 있는데 마지막 1위치가 5번째니까 5-3하면 2칸 움직여야 한다.

for i in range(n):
    for j in range(m):
        if box[5][i] == 1:
            ans[0].append(i - box[j][i].count('1'))
            # 0 대신 t
print(ans)
        