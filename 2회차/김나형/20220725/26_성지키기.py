from re import L
import sys
sys.stdin = open("26_성지키기.txt")

# n, m = map(int, input().split())
# li = []
# for _ in range(n):
#     li.append(input())

# row = 0
# col = 0

# for i in li:
#     if not 'X' in i:
#         row += 1
        
# for i in range(m):
#     if not 'X' in [li[j][i] for j in range(n)]:
#         col += 1
# print(max(row, col))

a, b = map(int, input().split())
lists = []

for _ in range(a):
    lists.append(input())#여기까지 입력

result1, result2 = 0, 0

for l in lists:
    if "X" not in l:
        result1 += 1#한 행씩 검사

for i in range(b):#한 열씩 검사하기 위해 for
    if "X" not in [lists[j][i] for j in range(a)]:
        result2 +=1

print(max(result1, result2))