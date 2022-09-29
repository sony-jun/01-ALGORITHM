# 백준 2750

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.




N = int(input())                    # 숫자를 입력

Number = []                         # 숫자들의 리스트를 생성

for _ in range(N):                  # 반복문을 통해 Number 리스트에 숫자 추가
    Number.append(int(input()))

Number.sort()                       # 리스트안에 있는 숫자들을 정렬

for i in range(len(Number)):        # 리스트안에 숫자들을 하나씩 출력
    print(Number[i])


