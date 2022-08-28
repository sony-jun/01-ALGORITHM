# 7568
""" 
1. 리스트에 나열된 사람의 덩치 정보를 이중 리스트(튜플)의 형태로 받는다.
2. 각 사람의 덩치 등수 정보를 저장하기 위해 기본값이 1인 리스트를 생성한다.
3. 덩치 정보 리스트를 순회하며 한 사람의 덩치를 각 사람과 비교한다.
4. 만일 현재 기준이 되는 사람의 덩치가 비교가 되는 사람의 덩치보다 크다면,
5. 비교가 되는 사람의 등수가 1씩 밀려난다.
"""
import sys
sys.stdin = open("덩치.txt")

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
# print(info)

# 덩치 등수를 저장할 리스트 생성(기본값은 1)
answer = [1] * N

for idx in range(len(info) - 1):