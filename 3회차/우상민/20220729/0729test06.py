# 신용카드만들기 2

T = int(input())
for i in range(1, T+1):
    N = list(input().replace('-',''))
    if len(N) == 16:
        if N[0] in '3''4''5''6''9':
            print(f'#{i}', 1)
        else:
            print(f'#{i}', 0)
    else:
        print(f'#{i}', 0)