test_case = int(input())

for _ in range(test_case):
    M, N = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(M)]
    sum = 0
    for i in range(N):
        lst_col = []
        lst_col = [lst[j][i] for j in range(M)]
        
        for k in range(len(lst_col)):
            if lst_col[k] == 1:
                continue
            elif lst_col[k] == 0:
                sum += lst_col[:k+1].count(1)

    print(sum)



