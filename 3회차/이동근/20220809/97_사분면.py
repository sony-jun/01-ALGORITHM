import sys

input = sys.stdin.readline

n = int(input())

quadrant = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
quadrant["AXIS"] = 0

for _ in range(n):
    x, y = map(int, input().split())

    if not x or not y:
        quadrant["AXIS"] += 1
    elif x > 0:
        if y > 0:
            quadrant["Q1"] += 1
        else:
            quadrant["Q4"] += 1
    else:
        if y > 0:
            quadrant["Q2"] += 1
        else:
            quadrant["Q3"] += 1

for q in quadrant:
    print(q, quadrant[q], sep=": ")