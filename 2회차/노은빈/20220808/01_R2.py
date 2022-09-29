import sys
input = sys.stdin.readline

r1, s = map(int,input().split())
r2 = 2*s - r1  #평균 구하는 식에서 반대로 구함
print(r2)