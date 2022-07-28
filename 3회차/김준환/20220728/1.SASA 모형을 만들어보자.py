# S모형 n개  A모형 m개
# 각각 2로 나눈 몫 값을 받아서 작은값 출력하면 된다

n, m = map(int, input().split())
print(min(n//2,m//2))