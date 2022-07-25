# https://www.acmicpc.net/problem/8958
# import sys

# sys.stdin = open("3_OX퀴즈.txt")

a = int(input())

for i in range(a) :
  ox = list(input())
  cnt = 0
  sum_cnt = 0

  for o in ox :
    if o == 'O' :
      cnt += 1
      sum_cnt += cnt
    
    else :
      cnt = 0

  print(sum_cnt)