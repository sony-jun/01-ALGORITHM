# import sys
# sys.sydin = open('성적통계_input.txt')

# 반 수
K = int(input())

# 반복문으로 반별 학생수 입력

for k in range(K):

    score = list(map(int, input().split()))
    student = score.pop(0)
    print(f'Class {k+1}')
    
    max_ = max(score)
    min_ = min(score)
    gap_list = []
    score.sort(reverse= True)
    
    for i in range(1, len(score)):
        gap_list.append(abs(score[i]-score[i-1]))
    print(f'Max {max_}, Min {min_}, Largest gap {max(gap_list)}')