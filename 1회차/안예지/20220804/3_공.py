# 1547.
"""
"""
N = int(input())
cup = [1, 2, 3]
for i in range(N):
    a, b = map(int, input().split())
    a_i = cup.index(a)
    b_i = cup.index(b)
    cup[a_i] = b
    cup[b_i] = a
print(cup[0])    