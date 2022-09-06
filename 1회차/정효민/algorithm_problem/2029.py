T = int(input())
for test_case in range(1 , 1 + T ):
    a , b = map(int , input().split())
    y = a / b
    x = a % b
    print(f'#{test_case} {int(y)}')