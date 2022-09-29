import sys
input = sys.stdin.readline

num = [int(input()) for i in range(10)]

print(sum(num)//10)
print(max(num, key = num.count))