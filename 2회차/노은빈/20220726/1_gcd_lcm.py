a,b = map(int,input().split())
#유클리드 호제법
#a>b가 있으면, a와 b의 최대공약수 G는 b와 a%b(a를 b로 나눈 나머지)의 최대공약수 G'과 서로 같다
def gcd(a, b):
    while b > 0:  #b가 0이 되는 순간 최대공약수
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)  #a, b로 나누는 수 중 가장 작은 수

print(gcd(a, b))
print(lcm(a, b))


#math 함수에 이미 최대공약수,최소공배수 구하는 함수가 있다!
import math
a, b = map(int, input().split())
print(math. gcd(a, b))
print(math. lcm(a, b))