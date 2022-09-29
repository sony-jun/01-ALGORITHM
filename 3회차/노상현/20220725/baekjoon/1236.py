n, m = map(int, input().split())    # n과 m을 받는다.
array = [input() for _ in range(n)]
row = 0 # row , col 을 초기화 해준다.
col = 0

for i in range(n): # 반복문을 실행하여, 리스트 형식의 값을 받아온 뒤 해당리스트에 'x' 값이 있는지 확인하는 조건문을 실행한다.
    if 'X' not in array[i]: # 리스트에 x가 있는지 확인후
        row += 1 # x 가 없을시 카운팅을 해준다.

for i in range(m): # 반복문을 실행하여, 리스트 형식의 값을 받아온 뒤 해당리스트에 'x' 값이 있는지 확인하는 조건문을 실행한다.
    if 'X' not in [array[k][i] for k in range(n)]:
        col += 1
        
        
print(max(row, col)) # 각각 경비