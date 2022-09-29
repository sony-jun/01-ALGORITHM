# 23825번 SASA 모형을 만들어보자

# S 모양 블록의 개수 N, A 모양 블록의 개수 M 받기
N, M = map(int,input().split())

# SASA 모형을 만드는 데에는 2개씩 필요하니까 2로 나누고
# 둘 중 작은 수만큼의 모형을 만들수 있으니까 결과 값에 넣어준다.
res = min(N//2, M//2)
print(res)