# https://www.acmicpc.net/problem/3052
# 문제3052번.나머지
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 10개의 줄에 하나의 정수가 주어짐
- 0 <= 정수 <= 1,000
'''



# 출력
'''
1. 42로 10개의 정수를 나누었을 때, 서로 다른 나머지가 몇개 있는지 출력
'''



# 코드
import sys

sys.stdin = open('input_text/3052.txt')

remainders = set()   # 중복 제거

for _ in range(10):
    remainders.add(int(sys.stdin.readline()) % 42)

print(len(remainders))



# 실행결과(메모리:30840KB, 시간:72ms)