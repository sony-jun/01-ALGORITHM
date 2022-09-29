# 8 X 8 체스판을 만들기
c = []

for _ in range(8) :

  # 각 행에서 말의 위치를 입력받기
  n = list(input())
  c.append(n)

# 검은색 칸에 말이 위치하면 cnt에 1을 더하기
# c[0][0]부터 번갈아가면서 흰색칸
# c[1][1]부터 번갈아가면서 흰색칸

c = []

for _ in range(8) :

  # 각 행에서 말의 위치를 입력받기
  n = list(input())
  c.append(n)

cnt = 0
for i in range(8) :
  for j in range(8) :
    if (i + j) % 2 == 0 :
      if c[i][j] == 'F' :
        cnt += 1

print(cnt) 