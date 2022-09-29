for _ in range(int(input())) :
    n, m = map(int, input().split())

    cnt = 0
    for i in range(n, m+1) :
        zero = str(i)
        cnt += zero.count('0')

    print(cnt)