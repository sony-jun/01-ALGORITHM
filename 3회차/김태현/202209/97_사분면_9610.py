import sys
sys.stdin = open("97_사분면_9610.txt", "r")

# 1사분면 (+ , +)
# 2사분면 (-, +)
# 3사분면 (- , -)
# 4사분면 (+ , -)
# 축 (? , 0), (0, ?)

data = {
    "Q1" : 0,
    "Q2" : 0,
    "Q3" : 0,
    "Q4" : 0,
    "AXIS" : 0,
}

tc = int(input())

for i in range(tc):
    x, y = map(int, input().split())
    
    if x > 0 and y > 0:
        data["Q1"] += 1
    elif x < 0 and y > 0:
        data["Q2"] += 1
    elif x < 0 and y < 0:
        data["Q3"] += 1
    elif x > 0 and y < 0:
        data["Q4"] += 1
    else:
        data["AXIS"] += 1

for k in data:
    print(f"{k}: {data[k]}")