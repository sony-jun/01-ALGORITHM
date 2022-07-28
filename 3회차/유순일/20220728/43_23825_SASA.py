import sys

sys.stdin = open('23825.txt', 'r')

s, a = list(map(int, input().split()))


# sasa 모형에 s 2개, a 2개.
s_ = s // 2
a_ = a // 2
# print(s_, a_)
# li = list(map(int(s_, a_)))
print(min(s_, a_))  