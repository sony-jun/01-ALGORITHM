matrix = [list(map(str,input())) for _ in range(8)] 
#comprehension 사용하여 이차원 리스트 만듦

result = 0  #하얀 칸 위에 말의 개수

for i in range(8) : #행의 개수만큼(칸 8개)
  for j in range(8) : #열의 개수만큼
    if (i+j) % 2 == 0 : #행과 열의 인덱스를 더한 후 2를 나눈 게 0이면 짝수(하얀 칸)
      if matrix[i][j] == 'F' : #하얀 칸에 'F'가 있다면
        result += 1  #+1을 해준다

print(result)