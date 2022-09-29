T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    numbers = list(map(int,input().split()))
    avg = sum(numbers)/n
    c = 0
    for i in range(n):
        if numbers[i] <= avg:
            c += 1
    result = c
    print(f'#{test_case}',result)
