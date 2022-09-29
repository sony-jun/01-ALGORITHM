# 최대공약수와 최소공배수 구함
# 유클리드 호제법 사용

# 최대공약수
def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a
# 최소공배수    
def lcm(a,b) :
    return int(a*b/gcd(a,b))

# 입력받은 자연수를 문자열 타입에서 정수형 타입으로 바꿈
a,b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))