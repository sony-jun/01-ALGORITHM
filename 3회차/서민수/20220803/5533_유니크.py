# 문제를 읽고 이해한다

# 행렬로 풀어야 할 지 그냥 int로 받아 풀어야 할 지
# 다만 각 행마다 중복되는 값이 있으면 포함하지 않고
# 중복되지 않다면 점수가 있다면 각 열에 점수를 더해주어라 라고 이해를 했다
# 3번을 게임 했고 참가자의 수가 N이라고 한다 
# N 행 3번의 게임은 열로 표현할 수 있을 것 같다

# 문제를 익숙한 용어로 재정의한다

# 행 N 열 M range, input
# for 반복문 set

# 어떻게 해결할지 계획을 세운다
# 행렬을 받고 행마다  세트를 사용해 중복값을 제고하고
# 열에 남은 점수들을 각각 더해준다?

# 프로그램으로 구현한다
from pprint import pprint
N = int(input())

lst = []
score_ = [0]*5
for i in range(N):
    unique = [list(input().split())for _ in range(N)]
    for j in range(i):
       score_ = lst.append(unique[j])

# 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다