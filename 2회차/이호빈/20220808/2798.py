from itertools import combinations
import sys
input = sys.stdin.readline
#입력값 받아주고
N, M = map(int, input().split())
#결과값을 받을 리스트
result = []
#입력값 받아줘
number = list(map(int, input().split()))

#combinations 함수 활용
combination = list(combinations(number, 3))
#for문 돌면서 만약 합이 블랙잭의 수보다 작거나 같다면 리스트에 추가해준다
for i in combination:
    if sum(i) <= M:
        result.append(sum(i))
#최댓값 출력
print(max(result))