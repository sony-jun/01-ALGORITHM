
n, m = map(int, input().split())

a = set(map(int, input().split())) # 집합 만들기
b = set(map(int, input().split())) # 집합 만들기

print(len(a-b) + len(b-a)) # 각 차집합을 더해줌
