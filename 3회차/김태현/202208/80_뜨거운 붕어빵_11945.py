import sys
sys.stdin = open("80_뜨거운 붕어빵_11945.txt","r")

n, m = map(int, input().split())

for _ in range(n):

    text = input()
    print(text[::-1])