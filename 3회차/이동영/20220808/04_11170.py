T = int(input())

for _ in range(T):
    cnt = 0
    a, b = map(int, input().split())

    for i in range(a, b+1):
        
        cnt += str(i).count('0')

    print(cnt)