import sys
sys.stdin = open('5800.txt')

T = int(input())

for i in range(1, T+1):
    gap = []
    score = list(map(int, input().split()))
    del score[0]
    score.sort()
    for j in range(len(score)-1):
        gap.append(score[j+1] - score[j])
    print(f'Class {i}')
    print(f'Max {max(score)}, Min {min(score)}, Largest gap {max(gap)}')
