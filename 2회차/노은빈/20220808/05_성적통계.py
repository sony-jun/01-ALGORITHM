import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t+1):
    score = list(map(int,input().split()))
    gap_list = []
    score.pop(0)  #맨 앞은 학생 수로 제외

    for j in range(len(score) - 1):
        score.sort(reverse=False)
        gap = score[j+1] - score[j]
        gap_list.append(gap)
    
    print(f'Class {i}')
    print(f'Max {max(score)}, Min {min(score)}, Largest gap {max(gap_list)}')
