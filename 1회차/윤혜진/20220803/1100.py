# https://www.acmicpc.net/problem/1100
# 문제1100번.하얀 칸
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 8x8크기의 체스판의 각 줄 당 체스판의 상태가 주어짐
- .: 빈칸
- F: 말이 있는 칸
'''



# 출력
'''
1. 하얀 칸 위에 말이 몇 개 있는지 출력
- 가장 왼쪽 위칸인 (0,0)위치는 하얀색 칸
- 체스판은 검정 칸과 하얀 칸이 번갈아 색칠되어 있음
'''



# 접근방법
'''
1. 각 칸을 (i,j) 좌표로 생각하자
2. 하얀 칸에 해당하는 (i,j)좌표의 각 값을 더하면, 짝수
3. 검정 칸에 해당하는 (i,j)좌표의 각 값을 더하면, 홀수
4. 따라서, i+j의 값이 짝수일때 F가 있으면, 1씩 카운트
'''



# 코드 1
import sys

sys.stdin = open('input_text/1100.txt')

# 8x8 크기의 체스판 만들기
matrix = [list(input()) for _ in range(8)]

# 하얀 칸 위에 말의 갯수 출력
cnt = 0
for r in range(8):
    for c in range(8):
        # 하얀 칸에 말이 있으면 카운트
        if (r + c) % 2 == 0 and matrix[r][c] == 'F':
            cnt += 1

print(cnt)



# 실행결과(메모리:30840KB, 시간:76ms)



# 코드 2
import sys

sys.stdin = open('input_text/1100.txt')

matrix = ''
for _ in range(8):
    matrix += input() + '0'

print(matrix[::2].count('F'))



# 실행결과(메모리:30840KB, 시간:76ms)