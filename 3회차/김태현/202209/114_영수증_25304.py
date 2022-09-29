import sys
sys.stdin = open("114_영수증_25304.txt", "r")


ans = int(input())
num = int(input())

result = 0

for i in range(num):
    a, b = map(int, input().split())
    result += a * b

if ans == result:
    print("Yes")

else:
    print("No")