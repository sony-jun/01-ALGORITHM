# 두 개의 자연수를 받아 최대 공약수와 최소 공배수를 출력
# 첫째 줄에는 두 개의 자연수가 주어진다

# 첫째 줄에는 입력으로 주어진 두 수의 최대 공약수를 출력
# 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력

n1, n2 = map(int, input().split())

# for문 최대공약수
for i in range(min(n1, n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        print(i)
        break
# n1, n2 중 가장 작은 숫자부터 1까지 -1을 하며 for문 실행
# 만약 n1 % i, n1 % i 값이 모두 딱 떨어져 나머지가 없는 상태라면
# 이때 사용된 i는 n1, n2의 최대 공약수

# for문 최소공배수
for i in range(max(n1, n2), n1 * n2+ 1):
    if i % n1 == 0 and i % n2 == 0:
        print(i)
        break
# n1, n2 중 더 큰 숫자부터 n1 * n2의 수까지 for문을 실행
# 더 큰 숫자부터 실행하는 이유는 n1, n2의 배수들 중
# 공통 부분을 찾는 것이기 때문에
# i % n1, i % n2 모두 값이 떨어지는 나머지가 없는 상태라면
# 이때 사용된 i는 n1, n2의 최소공배수



# 유클리드 호제법 최대공약수
def GCD(n1, n2):
    while(n2):
        n1, n2 = n2, n1 % n2
    return n1
print(GCD(n1, n2))
# while(n2) 가 True일 경우, 즉 n2가 0 초과일 경우
# n1의 자리에는 n2의 값을, n2의 자리에는 n1 % n2의 나머지 값인 r을 넣는다
# 그리고 다시 while문 반복
# n2가 0이 될때, 즉 n1를 n2로 나누어 떨어질 때
# 그 n2의 값은 n1, n2의 최대공약수

# 유클리드 호제법 최소공배수
def LCM(n1, n2):
    result = (n1 * n2) // GCD(n1, n2)
    return result
print(LCM(n1, n2))
# n1 * n2를 최대공약수로 나눈 몫이 최소공배수

# math 함수 최대공약수
import math
print(math.gcd(n1, n2))

# math 함수 최소공배수
print(math.lcm(n1, n2))