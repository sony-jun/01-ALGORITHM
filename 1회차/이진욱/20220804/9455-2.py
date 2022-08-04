T = int(input())

for t in range(T):

    N, M = map(int, input().split())

    S_list = [list(map(int, input().split())) for _ in range(N)]

    S_rev = [ [ 0 for i in range(N) ]  for _ in range(M)    ]

    real_ans = 0

    for i in range(M):
        for j in range(N):
            S_rev[i][j] = S_list[j][i]
        S_rev[i].reverse()

    for i in range(M):
        j_sum = 0
        cnt = 0
        for j in range(N):
            if S_rev[i][j] == 1:
                j_sum += j
                cnt += 1
        ans = j_sum - int((0.5*cnt*(cnt-1)))
        real_ans+=ans


    print(real_ans)

    # 기존 인덱스에서 정렬된 인덱스를 빼면 이동 횟수가 나오는 것을 이용하여 풀었다.
    