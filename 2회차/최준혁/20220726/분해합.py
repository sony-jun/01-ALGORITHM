N = int(input())
n = 0
for i in range(1, N+1): # 입력값의 범위 
    separate = list(map(int, str(i))) # 입력값을 분해
    hap = i + sum(separate) # i와 분해한 값을 더한다.
    if hap == N: # 합이 입력값과 같으면 
        n = i # n 변수에 i를 저장, 생성자가 없으면 0출력
        break

print(n) # i를 출력
