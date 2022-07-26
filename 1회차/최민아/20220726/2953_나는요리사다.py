import sys
sys.stdin = open("20220726/2953_나는요리사다.txt")

win_no = 0      # 우승자 번호
win_score = 0   # 우승자 점수

for i in range(1, 6):   # 참가번호 1~5번
    score = sum(list(map(int, input().split())))  # 평가점수의 합
    if score > win_score:   # 평가점수가 현재 우승자 점수보다 크면
        win_score = score   # 우승자 점수를 갱신
        win_no = i          # 우승자 번호도 갱신
    
print(win_no, win_score)    # 최종 우승자 번호와 점수 출력