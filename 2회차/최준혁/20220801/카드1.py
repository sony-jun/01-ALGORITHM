from collections import deque # deque 라이브러리 가져옴

N = int(input()) # 입력받을 정수값
d_que = deque() # deque를 담을 변수 생성

for i in range(1, N+1): # 1부터 N까지 1, 2, 3, 4, 5
    d_que.append(i) # deque에 추가

# deque의 길이가 1이 될때까지 반복
while len(d_que) != 1:
    l_pop = d_que.popleft() # 2, 3, 4, 5
    print(l_pop, end= ' ') # 1 출력
    l_pop = d_que.popleft() # 3, 4, 5
    d_que.append(l_pop) # 3, 4, 5, 2
print(d_que[0]) # 맨 마지막에 deque에 남은 값 출력  
