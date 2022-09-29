N = int(input()) # 입력값 입력
result = 0 # 입력값 N과 비교하기 위한 변수

for i in range(1, N + 1):
    A = list(map(int, str(i))) # str 함수를 통해 i의 각 자리 수를 A 리스트에 넣는다.
    result = i + sum(A) # i와 각 자리수가 들어간 A 리스트의 합
    if result == N: # 더한 값과 N 비교
        print(i)
        break
    if i == N: # 생성자가 없을 시 0 출력
        print(0)