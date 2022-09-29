import sys
sys.stdin = open('미로탐색_input.txt')
from pprint import pprint

N, M = map(int, input().split())

matrix = [input() for _ in range(N)]
pprint(matrix)