# N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램을 작성하라.
# 부르트포스 알고리즘

T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    count_zero = []
    counts = 0
    for i in range(N,M+1):
        count_zero.append(str(i))
    for i in count_zero:
        counts+=i.count('0')
    print(counts)