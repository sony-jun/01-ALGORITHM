# 최빈수를 출력하는 프로그램을 작성하여라

T = int(input())
counted = []
dict = {}
for i in range(1,T+1):
    order_i=int(input())
    n = list(map(int,input().split()))
    set_n = set(n)
    for j in set_n:
        dict[j]=n.count(j)
        counted.append(n.count(j))
        if dict[j]==max(counted):
            print("#%d %d" %(i, j))