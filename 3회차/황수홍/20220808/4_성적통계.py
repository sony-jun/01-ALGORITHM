K = int(input())

for i in range(K):
    score = list(map(int,input().split()))
    del score[0]
    score = sorted(score)
    print(f'Class {i+1}')
    gap = []

    for j in range(len(score)-1):
        gap.append(score[j+1] - score[j])
    
    print(f'Max {max(score)}, Min {min(score)}, Largest gap {max(gap)}')