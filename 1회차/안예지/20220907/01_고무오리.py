# 20001
"""
"""
# import sys
# sys.stdin = open("고무오리.txt")


stack = [input()]

while stack:
  order = input()

  if order == '고무오리 디버깅 끝' and len(stack) != 1:
    print("힝구")
    break
  
  elif order == '고무오리 디버깅 끝':
    print("고무오리야 사랑해")
    break
  
  if order == '고무오리' and len(stack) == 1:
    stack.append(order)
    stack.append(order)

  elif order == '고무오리':
    stack.pop()
    
  
  if order == '문제':
    stack.append(order)
    