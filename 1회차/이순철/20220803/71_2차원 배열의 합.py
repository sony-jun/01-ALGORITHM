# https://www.acmicpc.net/problem/2167

# 1줄 : n=행 m=열 
# 2줄~n줄 : m의 값 x <= 10000 
# 다음줄 : k = 합의 범위 
# 다음줄~k줄 : 좌표 *좌표는 (1,3),(2,3)이면 앞 수 1부터2까지 이며 뒷 수 3부터 3까지로 표현
# 모든 값들은 1 이상 인덱스도 1 이상으부터 시작 

from pprint import pprint
import sys
sys.stdin = open('71_2차원 배열의 합.txt')

n, m = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(n)]
# pprint(pan) 입력값들이 있는 2차원리스트
area = int(input())
area_list = [list(map(int, input().split())) for _ in range(area)]
# pprint(area_list) 합할 값들의 구역 좌표

cnt = 0
# 값을 더할 카운트
for h in range(area):
    i, j, x, y = area_list[h]
    # print(i, j, x, y)  좌표를 각각 할당
    for a in range(i-1, x):
    # 행의 좌표 구역 지정 [i-1] <= a <[x]
    # 인덱스 값은 [0]부터 시작이고 구역 좌표는 1부터 시작이라 [i-1]
        for b in range(j-1, y):
        # 열의 좌표 구역 지정 [j-1] <= b < [y] 
            cnt += pan[a][b]
            # 해당 좌표를 pan[][]인덱스에 넣어 반환값을 더하며 카운트
    print(cnt)
    cnt = 0
    # 더한 값을 출력하고 다음 구역 좌표 반복전 cnt 초기화

