Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0

for _ in range(int(input())):
    N, M = map(int, input().split())
    if N > 0 and M > 0:
        Q1 += 1
    elif N > 0 and M < 0:
        Q4 += 1
    elif N < 0 and M > 0:
        Q2 += 1
    elif N < 0 and M < 0:
        Q3 += 1
    elif N == 0 or M == 0:
        AXIS += 1
        
print(f"Q1: {Q1}")
print(f"Q2: {Q2}")
print(f"Q3: {Q3}")
print(f"Q4: {Q4}")
print(f"AXIS: {AXIS}")

