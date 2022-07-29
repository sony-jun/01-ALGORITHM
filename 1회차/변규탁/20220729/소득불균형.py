
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    incomes = list(map(int, input().split()))
    avg = sum(incomes) / len(incomes)

    answer = 0 
    for income in incomes:
        if income <= avg :
            answer += 1
    
    print(f'#{test_case} {answer}')

    
    

