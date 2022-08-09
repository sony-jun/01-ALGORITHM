
N = int(input())
for a in range(1,N+1):
    score = list(map(int, input().split()))
    new_score = sorted(score[1:])
    max_score = max(new_score)
    min_score = new_score[0]

    gap_list = []
    for t in range(len(new_score)-1):
        gap_list.append(abs(new_score[t]-new_score[t+1]))
    gap = max(gap_list)

    print(f'Class {a}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {gap}')