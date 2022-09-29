A, B = map(int, input().split())
a = set(list(input().split())) 
b = set(list(input().split())) # 중복값 제거, 대칭차집합에는 같은 값이 필요하지 않으므로

print(len(a - b) + len(b - a)) # a-b의 길이, b-a의 길이를 더함