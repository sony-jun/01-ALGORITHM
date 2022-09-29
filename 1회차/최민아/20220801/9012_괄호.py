T = int(input())

for test_case in range(T):
    PS = list(input())          # 괄호 문자열 입력
    sum = 0                     # 괄호가 올바른지 계산할 변수

    for i in PS:                # 괄호를 순서대로 탐색
        if i == "(":
            sum += 1            # 괄호가 ( 이면 +1
        elif i == ")":
            sum -= 1            # 괄호가 ) 이면 -1

        if sum < 0:             # (와 )의 개수가 짝을 이뤄야하는데 
            print("NO")         # )가 많을 경우 -1로 짝이 맞지 않음
            break
    
    if sum > 0:                 # 0보다 커도 (가 남는 것으로 짝이 맞지 않음
        print("NO")
    elif sum == 0:              # 마지막까지 0으로 맞아 떨어져야 VPS
        print("YES")