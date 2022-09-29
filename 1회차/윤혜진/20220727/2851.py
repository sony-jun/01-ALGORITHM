# https://www.acmicpc.net/problem/2851
# 문제2851번.슈퍼 마리오
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 10개의 줄에 각각 버섯의 점수가 주어짐
- 0 < 점수 <= 100
- 버섯이 나온 순서대로 점수가 주어짐
'''



# 출력
'''
1. 총 점수 출력
- 만약, 100에 가까운 수가 2개라면 큰 값을 선택
- 버섯을 순서대로 집음
- 중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없음
- 총 점수를 최대한 100에 가깝게 만들려고 함
'''



# 코드 1
import sys

sys.stdin = open('input_text/2851.txt')

mushrooms = [int(sys.stdin.readline().strip()) for _ in range(10)]   # 총 10개의 버섯

# 나올 수 있는 모든 점수 구하기
tot_scores = []
sum_score = 0   # 버섯을 먹어 점수를 더해나감
for i in range(0, 10):
    # 버섯을 먹지 않는 경우
    tot_scores.append(sum_score)
    # 버섯을 먹는 경우
    sum_score += mushrooms[i]

# 마지막 점수도 tot_scores에 추가
tot_scores.append(sum_score)

# 100점에 가장 가까운 점수 출력
min_diff = 100 * 10   # 최대 점수인 100점 x 버섯 갯수
rst = []   # 100점에 가장 가까운 점수
for score in tot_scores:
    if abs(100 - score) < min_diff:
        min_diff = abs(100 - score)
        rst.append(score) 
    elif abs(100 - score) == min_diff:
        rst.append(score)

print(max(rst))

# 실행결과(메모리:30840KB, 시간:72ms)



# 코드 2
sys.stdin = open('input_text/2851.txt')

score = int(input())

for _ in range(9):
    next = int(input())
    # |더하기 전의 점수 - 100|와 |더한 후의 점수 - 100|를 비교해 차이값이 더 적다면 더하기
    if abs(score - 100) >= abs((score + next) - 100):
        score += next
    else:
        print(score)
        break
# break 없이 끝났다면, 마지막까지 더한 점수가 100에 제일 가까움 
else:
    print(score)



# 실행결과(메모리:30840KB, 시간:72ms)
