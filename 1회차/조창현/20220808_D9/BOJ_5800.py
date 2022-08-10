import sys
sys.stdin = open('5800.txt')

K = int(input())  # K = 반의 수
for i in range(1, K + 1):
    score = list(map(int, input().split()))# 학생수와 시험점수
    del score[0]#첫번째는 점수아니므로 버림
    score.sort(reverse = True) # 내림차순 정렬
    diff = []
    print(f'class {i}')
    for x in range(len(score)-1):
        diff.append(score[x]-score[x+1]) # 만약 개수가 5개라면 i+1 이 4에서 끝나므로 i의 범위는 len(score-1)이다.
    print(f'Max {max(score)}, Min {min(score)}, Largest gap {max(diff)}')