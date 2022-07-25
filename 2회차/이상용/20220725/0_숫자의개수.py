# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

l = []
for i in range(3):
  l.append(int(sys.stdin.readline()))
print(l)
num = list(str(l[0]*l[1]*l[2]))

for j in range(10):
  print(num.count(str(j)))



# 일반적인 입력으로 진행할 때 ver
# a = int(input())
# b = int(input())
# c = int(input())
# result = list(str(a*b*c))

# for i in range(10):
#   print(result.count(str(i)))