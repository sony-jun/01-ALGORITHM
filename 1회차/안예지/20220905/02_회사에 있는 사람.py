# 7785

import sys
sys.stdin = open("회사.txt")

n = int(input())
logs = {}

for _ in range(n):
  log = input().split()
  name = log[0]
  logs[name] = log[1]

names = list(logs.items())
# print(names)
names = sorted(names, key = lambda x:x[0], reverse= True)
# print(names)

for idx in range(len(names)):
  name = names[idx][0]
  if names[idx][1] == 'enter':
    print(name)