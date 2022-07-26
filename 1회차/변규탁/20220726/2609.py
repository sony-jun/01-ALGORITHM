# 유클리드 호제법(구글찾아봄.)
# 1071은 1029로 딱 나눠지지 않기 때문에 1071을 1029로 나눈 나머지를 구함 -> 42
# 1029는 42로 딱 나눠지지 않기 때문에 1029를 42로 나눈 나머지를 구함 -> 21
# 42는 21로 나눠짐
# 최대공약수는 21


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

x, y = map(int, input().split())
print(gcd(x, y))
print(x*y//gcd(x,y))
