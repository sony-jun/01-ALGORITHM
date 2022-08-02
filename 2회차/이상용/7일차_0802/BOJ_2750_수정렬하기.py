# 1차 버전
N = int(input())
number_list = []
for i in range(N):
  number_list.append(int(input()))

number_list.sort()
# sorted(number_list)도 가능하며
# sorted(number_list)로 진행 시 하단부 for문도 sorted(number_list)로 작성해야함!

for j in number_list:
  print(j)

# 코드 간소화
number_list = [int(input()) for i in range(int(input()))]
for j in sorted(number_list):
  print(j)

# 리스트.sort() vs sorted(리스트) 차이점 정리
# 리스트.sort()는  본체의 리스트를 정렬해서 변환하는 것이고,
# sorted(리스트)는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환


