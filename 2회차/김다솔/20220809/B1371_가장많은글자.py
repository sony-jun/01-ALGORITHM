import sys
sys.stdin = open('B1371.txt')

while True:
    lines = sys.stdin.readlines()
    if not lines:
        break 
    print(lines