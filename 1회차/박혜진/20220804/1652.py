# n x n 모양의 방
# 짐을 피해서 연속해서 두칸의 자리가 있으면 누울 수 있다

# n의 값 입력받기
n = int(input())

# n x n의 2차원 배열 만들기
room = [list(input()) for _ in range(n)]

# 1. 행과 열을 분리해서 누울 수 있는 자리를 탐색하기
# 2. 누적합을 사용해서 X를 만나면 .의 값을 0으로 초기화

# 누울 수 있는 행 찾기

row = []
for i in range(n) :
  # 빈 공간의 수 저장할 리스트
  cnt = []
  # 빈 공간의 크기
  sizee = 0

  for j in range(n) :
    # 행의 요소가 빈 공간이라면 빈 공간의 크기에 1을 더한다
    if room[i][j] != 'X' :
      sizee += 1
    # 행의 요소가 빈 공간이 아니라면 지금까지 더한 빈 공간의 크기를 리스트에 저장하고
    # 빈 공간의 크기를 0으로 초기화한다
    else :
      cnt.append(sizee)
      sizee = 0
    # 행의 마지막 요소를 리스트에 저장
    cnt.append(sizee)

    # 빈 공간의 수를 저장한 리스트 요소 중 2 이상인 값만 행 리스트에 리스트로 저장
    row.append([r for r in cnt if r >= 2])

# 누울 수 있는 열 찾기

# 입력받은 n x n 2차원 행렬의 행과 열을 바꾸기
room_c = []

for i in range(n) :
  # 각 행의 i번째 열에 위치한 요소 저장할 리스트
  row_i = []
  for j in range(n) :
    # room에 저장되어있는 행렬의 요소를 열행으로 바꿔서 저장
    row_i.append(room[j][i])
  # 열행으로 바꾼 요소들을 새로운 행렬로 저장
  room_c.appned(row_i)

col = []
for i in range(n) :
  # 빈 공간의 수 저장할 리스트
  cnt1 = []
  # 빈 공간의 크기
  sizee1 = 0

  for j in range(n) :
    # 열의 요소가 빈 공간이라면 빈 공간의 크기에 1을 더한다
    if room_c[i][j] != 'X' :
      sizee1 += 1
    # 열의 요소가 빈 공간이 아니라면 지금까지 더한 빈 공간의 크기를 리스트에 저장하고
    # 빈 공간의 크기를 0으로 초기화한다
    else :
      cnt1.append(sizee1)
      sizee1 = 0
    # 열의 마지막 요소를 리스트에 저장
    cnt1.append(sizee1)

    # 빈 공간의 수를 저장한 리스트 요소 중 2 이상인 값만 열 리스트에 리스트로 저장
    col.append([r for r in cnt if r >= 2])

# 행 리스트와 열 리스트 안에 숫자가 저장된 요소들의 개수
row_cnt = 0

for i in row :
  row_cnt += int(len(i))

col_cnt = 0

for i in col :
  col_cnt += int(len(i))

print(row, col)