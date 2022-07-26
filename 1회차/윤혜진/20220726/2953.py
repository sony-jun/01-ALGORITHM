# https://www.acmicpc.net/problem/2953
# 문제2953번.나는 요리사다
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 첫번째 참가자가 얻은 4개의 평가 점수
...
5. 다섯번째 참가자가 얻은 4개의 평가 점수
'''



# 출력
'''
1. 우승자의 번호, 우승자가 얻은 점수 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/2953.txt')

winner_score = 0   # 우승자의 점수
winner_num = 0   # 우승자의 번호
# 1번부터 5번 참가자까지 순서대로 4개 평가 점수를 모두 합하기
for i in range(1, 5 + 1): 
    tot_score = sum(map(int, input().split()))
    # 이전 참가자들의 점수 최댓값보다 현재 참가자의 점수가 더 높은 경우, 갱신
    if winner_score < tot_score:
        winner_num = i
        winner_score = tot_score

print(winner_num, winner_score)



# 실행결과(메모리:30840KB, 시간:72ms)
