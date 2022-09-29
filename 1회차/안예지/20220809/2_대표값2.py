# 2587.
""" 
"""
import heapq

# 입력받은 숫자들을 저장할 리스트 생성
numbers = list(int(input()) for _ in range(5))
# 힙으로 빼오기 전 평균을 구해주기
avg = sum(numbers)//5

# 리스트 힙으로 만들어 재정렬
heapq.heapify(numbers)
# 중간값 후보들을 저장할 리스트
middle = []
# 입력 숫자들이 저장된 리스트를 순회하며 중간값 후보 리스트에 재정렬해주기
for _ in range(len(numbers)):
    middle.append(heapq.heappop(numbers))
print(avg)
print(middle[2])