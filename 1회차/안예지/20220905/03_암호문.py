# swea 1228

import sys
sys.stdin = open("암호문.txt")

# 원본 암호문

# print(password)

for t in range(1, 11):
  N = int(input())
  password = input().split()
    
  # 명령문
  M = int(input())
  order = input().split()
  # print(order)

  # 명령문을 돌면서 'I'가 발생할 때마다
  for idx in range(len(order)):
    if order[idx] == 'I':
      x = int(order[idx + 1])
      y = int(order[idx + 2])
      
      for how in range(y, 0, -1):
        password.insert(x, order[idx + 2 + how]) 
        
  print(f'#{t}', end=" ")
  print(*password[:10])