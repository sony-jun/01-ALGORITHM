t = int(input())
for _ in range(1,t+1):
    n,m = map(int,input().split())
    numbers = list(range(n,m+1))
    cnt=0
    for number in numbers:
        cnt+=str(number).count('0')
    print(cnt)