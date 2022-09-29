n ,m = map(int, input().split()) # 행의 개수, 열의 개수 입력

parking = [] # 빈 리스트 생성

for _ in range(n): # 행의 개수만큼 반복
    parking.append(input()) # 문자열 입력 받은 것을 parking리스트에 추가


print(parking)