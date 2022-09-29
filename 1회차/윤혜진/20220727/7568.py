# https://www.acmicpc.net/problem/7568
# 문제7568번.덩치
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 전체 사람의 수 N
2. N개의 줄에는 각 사람의 몸무게 x와 키 y가 입력됨
- 2 <= N <= 50
- 10 <= x,y <= 200
'''



# 출력
'''
1. 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 한 줄에 출력
- 각 덩치 등수는 공백문자로 분리
- 덩치 등수 = N명 중 자신보다 더 큰 덩치를 가진 사람의 수 + 1
<덩치 비교 방법>
- 자신의 몸무게, 키보다 각각 모두 커야, 덩치가 자신보다 큰 사람임
- 몸무게와 키 중 하나만 크면, 덩치를 비교할 수 없음
'''



# 코드 1
import sys

sys.stdin = open('input_text/7568.txt')

N = int(input())   # 사람 수

# 사람마다 키와 몸무게 값을 입력받아 각각 다른 리스트에 담기
heights = []
weights = []
for _ in range(N):
    height, weight = map(int, sys.stdin.readline().split())
    heights.append(height)
    weights.append(weight)

# 사람마다 덩치 등수 구하기
size_ranking = []   # 각 사람당 덩치 등수
for i in range(0, N):   # 덩치 비교할 대상
    cnt = 1   # 자신보다 덩치가 큰 사람 수
    for j in range(0, N):   # 덩치 비교할 상대방
        # 비교할 상대방이 자기 자신이면, 넘어가기
        if i == j:
            continue
        elif heights[i] < heights[j] and weights[i] < weights[j]:
            cnt += 1
    size_ranking.append(cnt)
print(*size_ranking)



# 실행결과(메모리:30840KB, 시간:68ms)



# 코드 2
import sys

sys.stdin = open('input_text/7568.txt')

N = int(input())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for me_idx in range(len(info)):
    cnt = 1
    for other_idx in range(len(info)):
        if info[me_idx][0] < info[other_idx][0] and info[me_idx][1] < info[other_idx][1]:
            cnt += 1
    print(cnt, end=' ')



# 실행결과(메모리:30840KB, 시간:68ms)