import sys
sys.stdin = open("9. 로봇.txt", "r")
from pprint import pprint
M , n = map(int,input().split())

robot = [[0]* M for _ in range(M)]
pprint(robot)