import sys
sys.stdin = open("23825.txt")
n, m = map(int, input().split())
print(min(n, m)//2)