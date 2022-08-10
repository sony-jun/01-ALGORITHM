import sys
sys.stdin = open("20220810/4963_섬의개수.txt")

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break