# n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력해야 한다.

T = int(input())

for i in range(1, T+1):
    N = int(input())
    income = list(map(int,input().split()))
    
    cnt = 0
    for j in income:
        if j <= sum(income)/N:
            cnt += 1

    print(f'#{i} {cnt}')