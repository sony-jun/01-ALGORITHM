import sys
sys.stdin = open('B1269.txt')

a, b = map(int, input().split())
set_a = set(input().split())
set_b = set(input().split())
# print(set_a)
# print(len(set_a - set_b)+len(set_b - set_a))
print(len(set_a^set_b))
#len((A_set - B_set) | (B_set - A_set))