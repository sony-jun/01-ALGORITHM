a, b = map(int, input().split()) # input 값 

matrix = [list(input()) for _ in range(a)] # matrix 에 배열 list?를 넣는다

cnt = 0 # 갯수 카운트 0

for i in matrix: # 매트릭스 를 반복
    for
        if 'X' not in i: # 만약 X가 매트릭스를 순서대로 지나는 것에 없다면
            cnt += 1 # 카운트 + 1
        
print(cnt) # 프린트 카운트