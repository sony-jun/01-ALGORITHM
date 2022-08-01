# 2161.
"""
"""
from collections import deque

n = int(input())
# 입력받은 번호까지의 카드를 저장할 리스트
n_list = deque(range(1, n +1))

while len(n_list) > 1:
    print(n_list.popleft(), end =" ")
    n_list.append(n_list.popleft())
    
print(n_list[0])

