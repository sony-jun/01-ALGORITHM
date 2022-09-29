n, m = map(int, input().split())

# 집합에 정수 저장
a = set(map(int, input().split()))
b = set(map(int, input().split()))

# a와 b의 차집합 길이와 b와 a의 차집합 길이 더하기
print(len(a - b) + len(b - a))