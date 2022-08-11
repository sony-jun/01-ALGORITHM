import sys

sys.stdin = open("_2979.txt", "r")

arr = [0] * 101

A, B, C = map(int, input().split())

for _ in range(3):
    i, o = map(int, input().split())
    for time in range(i, o):
        arr[time] += 1
    
    answer = 0
    for time in arr:
        if time == 0:
            continue
        elif time == 1:
            answer += A*1
        elif time == 2:
            answer += B*2
        elif time == 3:
            answer += C*3

print(answer)

