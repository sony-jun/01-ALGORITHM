T = int(input())
scores = [0]*101

for i in range(T):
    t = input()
    score = map(int, input().split())
    for j in score:
        scores[j] += 1

    mode = 0
    for k in range(101):
        if scores[k] == max(scores):
            mode = k

    print(f'#{t} {mode}')