n,m = map(int,input().split())
fish = [list(input()) for i in range(n)]

for i in range(n):
    fish[i] = fish[i][::-1]
    print(*fish[i],sep='')
