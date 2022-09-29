T = int(input())
totalList = []

for t in range(T):
    s = int(input())  # 차 가격
    n = int(input())  # 옵션 수
    total = 0
    optotal = 0

    for _ in range(n):
        p, q = map(int, input().split())
        optotal += p * q
    total = s + (optotal)
    totalList.append(total)

for i in totalList:
    print(i)
