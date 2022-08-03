
# 세로(열) : N 가로(행) : M의 숫자 입력받기
n, m = map(int, input().split())

c = []
col, row = 0, 0
# 입력받은 열(N)의 숫자만큼 경비원 위치 입력받기
for i in range(n) :
  s = list(input())
  c.append(s)

  # 해당 행에 X가 없으면 1을 더하기
  if 'X' not in c[i] :
    col += 1

# N X M의 행렬을 M X N의 행렬로 모양을 변환하여 행에 X가 없으면 1을 더하기
for j in range(m) :
    if 'X' not in [c[i][j] for i in range(n)] :
        row += 1

print(max(col, row))