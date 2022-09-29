# https://www.acmicpc.net/problem/23825
# 문제23825번.SASA 모형을 만들어보자
# 시간제한:0.5초, 메모리제한:512MB



# 입력
'''
1. 알파벳 S모양의 블록 갯수 N, 알파벳 A모양의 블록 갯수 M
- 1 <= N, M <= 10^9
'''



# 출력
'''
1. SASA 모형 갯수의 최댓값 출력
- SASA모형 1개 = 알파벳 S 블록 2개 + 알파벳 A 블록 2개 
'''



# 코드
import sys

sys.stdin = open('input_text/23825.txt')

S, A = map(int, input().split())

# S블록과 A블록이 1대1일 때만 모형을 만들 수 있으므로
# 둘 중 더 작은 블록 수를 구한 후, 2로 나눠 모형 하나를 만듦
print(min(S, A) // 2)



# 실행결과(메모리:30840KB, 시간:76ms)