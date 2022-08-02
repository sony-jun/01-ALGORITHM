# https://www.acmicpc.net/problem/1269
# 문제1269번.대칭 차집합
# 시간제한:2초, 메모리제한:256MB



# 입력
'''
1. 집합 A의 원소 갯수, 집합 B의 원소 갯수
- 0 < 원소 갯수 <= 200,000
2. 집합 A의 모든 원소
3. 집합 B의 모든 원소
- 0 <= 원소의 값 <= 100,000,000
'''



# 출력
'''
1. 대칭 차집합의 원소 갯수
'''



# 코드 1
import sys

sys.stdin = open('input_text/1269.txt')

An, Bn = map(int, input().split())
A = set(input().split())
B = set(input().split())

print(len(A ^ B))



# 실행결과(메모리:104120KB, 시간:264ms)



# 코드 2
import sys

sys.stdin = open('input_text/1269.txt')

An, Bn = map(int, input().split())
A = input().split()
B = input().split()

print(2 * len(set(A + B)) - len(A) - len(B))



# 실행결과(메모리:87424KB, 시간:204ms)