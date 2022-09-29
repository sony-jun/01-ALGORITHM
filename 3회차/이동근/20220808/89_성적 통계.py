T = int(input())

for i in range(T):
    score = list(map(int, input().split()))

    N = score[0]
    score = score[1:]
    
    score.sort(reverse=True)

    gap = max([abs(score[j] - score[j + 1]) for j in range(N - 1)])

    print(f"Class {i + 1}")
    print(f"Max {score[0]}, Min {score[-1]}, Largest gap {gap}")