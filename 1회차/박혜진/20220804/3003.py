# 3003

# 체스 말의 구성 8개의 검은 말과 8개의 흰색 말
# 8개의 말 종류 : 킹(1), 퀸(1), 룩(2), 비숍(2), 나이트(2), 폰(8)

# 발견한 흰색 말의 개수를 입력받기
k, q, r, b, n, p = map(int, input().split())

# 입력받은 수는 0 <= 수 <=10

if k - 1 != 0 :
  print(-(k - 1), end=' ')
else :
  print(0, end=' ')

if q - 1 != 0 :
  print(-(q - 1), end=' ')
else :
  print(0, end=' ')

if r - 2 != 0 :
  print(-(r - 2), end=' ')
else :
  print(0, end=' ')

if b - 2 != 0 :
  print(-(b - 2), end=' ')
else :
  print(0, end=' ')    

if n - 2 != 0 :
  print(-(n - 2), end=' ')
else :
  print(0, end=' ')

if p - 8 != 0 :
  print(-(p - 8), end=' ')
else :
  print(0, end=' ')