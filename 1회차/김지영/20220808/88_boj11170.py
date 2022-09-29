T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    cnt = 0
    for i in range(n,m+1):
        i = str(i)
        cnt += i.count('0')
    result = cnt
    print(result)