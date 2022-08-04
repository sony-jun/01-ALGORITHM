import sys
from pprint import pprint

sys.stdin = open("2_박스.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    n, m = map(int, sys.stdin.readline().split())
    cell = [[*map(int, sys.stdin.readline().split())]for _ in range(n)]
    
    print(cell)