M = int(input())

def bunhaehap(N):                           # 분해합 함수 작성
    input_number = N                        # 입력값을 따로 할당 (나중에 활용)
    sum_rest = 0                            # 나머지 값 초기화
    while input_number != 0:                # 입력값이 0이 되면 자동으로 작동 중지
        sum_rest += input_number % 10       # 10으로 나눈 나머지를 합함
        input_number //= 10                 # 입력값을 10으로 나눈 몫으로 할당
    result = N + sum_rest                   # 나머지와 입력값을 더함
    return result                           # 그 값을 반환
    
for i in range(1, M + 1):                   # 최소값을 찾기 위해 1부터 입력값까지 순회
    if bunhaehap(i) == M:                   # 순회하며 분해합 함수 적용, 그 값이 입력값과 같게 되면, 제일 작은 생성자가 됨.
        print(i)
        break                               # 출력후에도 반복하지 않게 break
    elif i == M:                            # 생성자가 없다면 i는 range의 마지막 숫자인 M에 도달한다. 그 때는 0을 출력한다.
        print(0)
