import sys

sys.stdin = open("1_분해합.txt")

n = input() # 256

total = 0

for i in range(1, int(n) + 1):
    for j in str(i):
        total += int(j)
    total += int(i)
    if total == int(n):
        print(i)
        break
    else:
        total = 0
else:
    print(0)