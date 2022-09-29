from sys import stdin

dict = {}
lst = []

a,b = map(int, stdin.readline().split())

# 집합 A와 집합 B의 원소를 list에 모두 삽입
lst.extend(stdin.readline().split())
lst.extend(stdin.readline().split()) # lst = [1,2,4,2,3,4,5,6]

# A와 B집합의 원소가 모두 삽입된 리스트에서 for문 돌려서 중복이 없는 원소만 값을 1로 지정
for i in lst:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

count = 0

# 리스트 중에서 중복되지 않는 원소만 count하여 출력
for j in dict: 
    if dict[j] == 1: 
        count += 1 # [1,3,5,6]

print(count)