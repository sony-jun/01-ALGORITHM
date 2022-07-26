a, b = map(int, input().split())

# 유클리드 호제법

# 최대공약수
def gcd(a, b):
    # 계속 나누다가 b가 0이되면
    if b == 0:
        # 최대공약수는 a
        return a
    # a를 b로 나눠서 나머지를 b에 대입
    # b는 다시 a가 됨
    return gcd(b, a % b)

# 최대공약수
print(gcd(a, b))
# 최소공배수 : a와 b를 곱하고 최대공약수로 나눔
print(a*b // gcd(a, b))