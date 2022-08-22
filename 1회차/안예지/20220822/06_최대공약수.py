# 2609
"""
"""
import sys
sys.stdin = open("최대공약수.txt")

a, b = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        
    return a

def lcd(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b), lcd(a, b), sep = '\n')