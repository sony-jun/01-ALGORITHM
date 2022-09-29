# 모든 옵션이 주어진 자동차를 구매하는데 필요한 액수를 계산해 주자.

T = int(input())
for i in range(T):
    opt=0
    s = int(input())
    n = int(input())
    for i in range(n):
        qp = list(map(int,input().split()))
        q=qp[0]
        p=qp[1]
        opt+=q*p
    price = s+opt
    print(price)