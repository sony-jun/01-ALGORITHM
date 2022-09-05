# 1157

import sys
sys.stdin = open("단어공부.txt")

# 입력값 받아오기
words = input().upper()
wordict = {}
for key in words:
  wordict[key] = wordict.get(key, 0) + 1

answer = list(wordict.items())

answer = sorted(answer, key = lambda x:-x[1])
# print(answer)

max_ = answer[0][1]

if list(wordict.values()).count(max_) == 1 :
  print(answer[0][0])
  
else:
  print('?')