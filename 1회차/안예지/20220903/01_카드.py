# 11652
"""
"""
import sys
sys.stdin = open("카드.txt")

def bsearch(arr, target, left_, right_):
  
  while left_ <= right_:
    
    mid = (left_ + right_) // 2
    
    if target == arr[mid]:
      return arr[mid]
    
    elif target > arr[mid]:
      left_ = mid + 1
      
    elif target < arr[mid]:
      right_ = mid - 1
      
  return arr[mid]

N = int(input())
have = list(map(int, [input() for _ in range(N)]))
have = sorted(have)
# print(have)

count_dict = {}
for element in have:
  number = bsearch(have, element, 0, len(have) - 1)
  count_dict[element] = count_dict.get(number, 0) + 1

# print(count_dict)

values = list(count_dict.items())
values = sorted(values, key=lambda x:(-x[1],x[0]))

# print(values)

print(values[0][0])