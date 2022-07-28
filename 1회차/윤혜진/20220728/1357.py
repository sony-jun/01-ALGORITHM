# https://www.acmicpc.net/problem/1357
# 문제1357번.뒤집힌 덧셈
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. X, Y
- 0 < X, Y <= 1,000
'''



# 출력
'''
1. Rev(Rev(X) + Rev(Y))의 정답을 출력
- Rev()함수: 자연수 X의 모든 자리수를 역순으로 만드는 함수
'''



# 코드 
import sys

sys.stdin = open('input_text/1357.txt')

def rev(num: str):
    return num[::-1].lstrip('0')

n1, n2 = input().split()
print(rev(str(int(rev(n1)) + int(rev(n2)))))



# 실행결과(메모리:30840KB, 시간:68ms)