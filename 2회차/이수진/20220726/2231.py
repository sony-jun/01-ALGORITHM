n = int(input()) # 예시 : 123


for i in range (1, n+1) : #1부터 123까지 검사 
    temp = []
    for j in str(i) : # 문자열 i에 대해서 검사
        temp.append(j) # 빈 리스트에 i넣기
        result = list(map(int, temp)) # 리스트 요소 정수형으로 변환
    if n == sum(result)+i : # 입력값이 리스트요소합+i이면 출력
        print(i)
        break
    if i == n : # i가 123에 도달할때까지 답이 안나오면 0출력
        print(0)