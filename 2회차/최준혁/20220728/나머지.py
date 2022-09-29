A = []
cnt = 0

for i in range(10):
    N = int(input()) # 10번 입력
    A.append(N%42) # 입력값을 42로 나눠서 리스트에 저장

A = len(set(A)) # 중복제거한 길이 얻어냄
print(A) # 출력