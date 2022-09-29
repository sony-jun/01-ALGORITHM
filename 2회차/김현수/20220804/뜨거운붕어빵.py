import sys
sys.stdin = open('뜨거운붕어빵.txt')
from pprint import pprint

N, M = map(int,input().split())

for _ in range(N):
    fish = input() #문자열로 방는다
    print(fish[::-1])