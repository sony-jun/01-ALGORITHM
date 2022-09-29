# 9610.
"""
접근방법

"""
n = int(input())
q_dict = {}

for idx in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        q_dict[1] = q_dict.get(1, 0) + 1
    if x < 0 and y > 0:
        q_dict[2] = q_dict.get(2, 0) + 1
    if x < 0 and y < 0:
        q_dict[3] = q_dict.get(3, 0) + 1
    if x > 0 and y < 0:
        q_dict[4] = q_dict.get(4, 0) + 1
        
axis = n - sum(q_dict.values())
        
print(f'Q1: {q_dict.get(1, 0)}')
print(f'Q2: {q_dict.get(2, 0)}')
print(f'Q3: {q_dict.get(3, 0)}')
print(f'Q4: {q_dict.get(4, 0)}')
print(f'AXIS: {axis}')
