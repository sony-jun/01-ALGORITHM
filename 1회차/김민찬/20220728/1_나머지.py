rest = [] # rest라는 빈 배열 생성

for i in range(10):
    N = int(input())
    rest.append(N % 42) # append를 사용해서 배열의 마지막에 원소 추가

rest = set(rest) # 중복 제거를 위해 set 함수 사용
print(len(rest)) # rest의 길이 출력(len)