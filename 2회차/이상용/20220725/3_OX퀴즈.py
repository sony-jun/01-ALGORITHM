# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

l = []
for i in range(6):
  l.append(sys.stdin.readline().strip('\n')) # ['5', 'OOXXOXXOOO', 'OOXXOOXXOO', 'OXOXOXOXOXOXOX', 'OOOOOOOOOO', 'OOOOXOOOOXOOOOX']
T = int(l[0])
for i in range(T):
  score = 0
  sumscore = 0
  for j in l[1:7]:
    for k in j:
      if k == 'O':
        score += 1
      else:
        score = 0
    sumscore += score
  print(sumscore)

# 일반적인 입력으로 진행할 때
# T = int(input())
# for i in range(T):
#     a = input()
#     score = 0
#     sumScore = 0
#     for j in a:
#         if j == 'O':
#             score += 1
#         else:
#             score = 0
#         sumScore += score
#     print(sumScore)