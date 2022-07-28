import sys
sys.stdin = open("3_쉽게푸는문제.txt", 'r')

A, B = map(int, input().split())

i = 1
s = []
res = 0

while i <= B:
    for n in range(1, i+1):
        s.append(i)
    i += 1

for n in s[A-1:B]:
    res += n
    
print(res)