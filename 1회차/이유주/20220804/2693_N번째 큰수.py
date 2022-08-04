#목록에서 세번째 큰수 찾는 문제
T = int(input())
for i in range(T):
    num = list(map(int, input().split()))
    num.sort()
    print(num[-3])