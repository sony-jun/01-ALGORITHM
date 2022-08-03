import sys

sys.stdin = open("input.txt", "r")

n, m = map(str,input().split())

min_1 = n.replace('6','5')
min_2 = m.replace('6','5')

max_1 = n.replace('5','6')
max_2 = m.replace('5','6')

print(int(min_1) + int(min_2), int(max_1) + int(max_2))
