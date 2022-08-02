T = int(input())

sum_ = 0
cnt = 0

for i in range(1,T+1):
    N = int(input())
    list_ = [0 for i in range(N)]
    list_ = list(map(int, input().split()))
    sum_ = sum(list_)
    avg = sum_/(N)

    for j in range(N):
        if list_[j] <= avg:
            cnt +=1
    print(f'#{i} {cnt}')
    cnt = 0