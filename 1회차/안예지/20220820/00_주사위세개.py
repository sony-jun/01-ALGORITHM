# 2480.
"""
"""
import sys
sys.stdin = open("주사위.txt")

a, b, c = map(int, input().split())

# 같은 눈이 3개가 나오면 
if a == b and a == c:
    print(10000 + a * 1000)

# 같은 눈이 2개가 나오는 경우
elif a == b and a != c:
    print(1000 + a * 100)

elif b == c and a != b:
    print(1000 + b * 100)
    
elif c == a and b != a:
    print(1000 + a * 100)
    
else:
    print(max(a, b, c) * 100)
