import sys
sys.stdin = open('test.txt', 'r')

one, two, three = list(map(int, input().split()))
time = [0 for _ in range(100)]
for i in range(3):
    start, end = list(map(int, input().split()))
    for j in range(start, end):
        time[j] += 1
fee = time.count(1) * one + time.count(2) * two * 2 + time.count(3) * three * 3
print(fee)