# 유클리드 호제법 - 재귀

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
