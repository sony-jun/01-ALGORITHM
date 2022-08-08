# https://www.acmicpc.net/problem/2309
# 문제2309번.일곱 난쟁이
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 9개 줄에 난쟁이들의 키
- 0 < 키 <= 100
'''



# 출력
'''
1. 일곱난쟁이의 키를 오름차순으로 출력
- 9명의 난쟁이 중 일곱난쟁이를 찾아야함
- 일곱난쟁이의 키를 모두 합하면 100이 됨
- 정답이 여러개인 경우, 아무거나 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/2309.txt')

def find_7_shorts(start, shorts_7):   # 일곱난쟁이 찾기
    global rst, heights

    # 7명의 키를 모두 선택한 경우, 합을 확인하고 리턴
    if len(shorts_7) == 7:
        if sum(shorts_7) == 100:
            rst = shorts_7
        return 

    # 중복되지 않게 한 명씩 선택
    for idx in range(start, 9):
        find_7_shorts(idx + 1, shorts_7 + [heights[idx]])


# 9명 난쟁이의 키를 모두 기록
heights = [int(input()) for _ in range(9)]

# 일곱난쟁이의 키를 오름차순으로 출력
rst = []
find_7_shorts(0, [])
for h in sorted(rst):
    print(h)



# 실행결과(메모리:30840KB, 시간:68ms)



# 코드 2
import sys
from itertools import combinations

sys.stdin = open('input_text/2309.txt')

# 9명 난쟁이의 키를 모두 기록
heights = [int(input()) for _ in range(9)]

# 일곱난쟁이의 키를 오름차순으로 출력
shorts_7 = [case for case in combinations(heights, 7) if sum(case) == 100]

for h in sorted(shorts_7[0]):
    print(h)



# 실행결과(메모리:30840KB, 시간:68ms)



# 코드 3
import sys

sys.stdin = open('input_text/2309.txt')

# 9명 중 7명 찾기 = 9명 중 2명 빼기
def find_7_shorts(shorts_9):
    for i in range(0, 7 + 1):
        for j in range(i + 1, 8 + 1):
            if sum(shorts_9) - shorts_9[i] - shorts_9[j] == 100:
                # 인덱스 i, j 위치의 값을 제거한 리스트 구하기
                shorts_7= []
                for k in range(9):
                    if k != i and k != j:
                        shorts_7.append(shorts_9[k])
                return shorts_7


# 9명 난쟁이의 키를 모두 기록
heights = [int(input()) for _ in range(9)]

# 일곱난쟁이의 키를 오름차순으로 출력
shorts_7 = find_7_shorts(heights)
for h in sorted(shorts_7):
    print(h)



# 실행결과(메모리:30840KB, 시간:76ms)