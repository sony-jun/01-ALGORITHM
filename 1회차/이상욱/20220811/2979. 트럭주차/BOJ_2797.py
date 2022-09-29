import sys
sys.stdin = open('2797.txt')

A, B, C = map(int, input().split())
time = [0] * 100

for i in range(3):
    a, b = map(int, input().split())
    for j in range(a, b):
        time[j] += 1
# print(time)
sum_a = (1 * time.count(1) * A)
sum_b = (2 * time.count(2) * B)
sum_c = (3 * time.count(3) * C)
#print(sum_a, sum_b, sum_c)
print(sum_a + sum_b + sum_c)