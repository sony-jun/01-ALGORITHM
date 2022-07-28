# SASA 모형을 만들어보자
# 문제 : SASA 모형 개수의 최댓값을 출력하기
#       모형 1개는 S, A가 각각 2개씩 필요
# 접근 : 더 작은 수를 찾아서 모형에 필요한 개수인 2로 나누기

S, A = map(int, input().split())

result = min(S, A)

print(result // 2)
