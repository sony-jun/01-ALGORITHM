# https://www.acmicpc.net/problem/2609
# 문제2609.최대공약수와 최소공배수
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 두개의 자연수
- 0 < 자연수 <= 10,000
'''



# 출력
'''
1. 두 수의 최대공약수 (Greatest common divisor, GCD)
2. 두 수의 최소공배수 (Least common multiple, LCM)
'''



# 코드 1
import sys

sys.stdin = open('input_text/2609.txt')

n1, n2 = map(int, input().split())

# 공약수(두 수에 모두 나누어떨어지는 수) 구하기
# 1부터 두 자연수 중 작은 수까지 돌면서 공약수 구하기
common_div = []
for div in range(1, min(n1, n2) + 1):
    if n1 % div == 0 and n2 % div == 0:
        common_div.append(div)

# 최대공약수 구하기
gcd = common_div[-1]
print(gcd)

# 최소공배수 구하기
lcm = gcd * (n1 // gcd) * (n2 // gcd)
print(lcm)



# 실행결과(메모리:30840KB, 시간:76ms)



# 코드 2 - 유클리드 호제법
# 2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 참고(유클리드 호제법 ): https://ko.m.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95
# 참고(유클리드 호제법): https://velog.io/@yerin4847/W1-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95

sys.stdin = open('input_text/2609.txt')

def gcd(n1, n2):
    # 나머지가 0일때, 나눈 수가 최대공약수
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)

n1, n2 = map(int, input().split())
# 최대공약수 구하기
print(gcd(n1, n2))
# 최소공배수 구하기
print(n1 * n2 // gcd(n1, n2))



# 실행결과(메모리:30840KB, 시간:68ms)



# 코드 3 - 표준 함수 사용
from math import gcd

sys.stdin = open('input_text/2609.txt')

n1, n2 = map(int, input().split())

GCD = gcd(n1, n2)
LCM = n1 * n2 // GCD

print(GCD)
print(LCM)



# 실행결과(메모리:32952KB, 시간:72ms)