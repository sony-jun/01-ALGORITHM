T = int(input())
for _ in range(T):
    answer = int(input())
    n = int(input())
    for i in range(n):
        p, q = map(int, input().split())
        answer += p * q
    print(answer)