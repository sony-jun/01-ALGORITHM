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
# pprint(pan)
area = int(input())
area_list = [list(map(int, input().split())) for _ in range(area)]
# pprint(area_list)

cnt_list = []
for h in range(area):
    i, j, x, y = area_list[h]
    a = [pan[i-1][j-1] for j in range(1,m+1)]
    b = [pan[x-1][y-1] for y in reversed(range(1,m+1))]
    print(a,b,sep='\n')