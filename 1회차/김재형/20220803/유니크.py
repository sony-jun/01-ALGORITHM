from platform import platform
import sys
sys.stdin = open('유니크_input.txt')

# 5
# 100 99 98
# 100 97 92
# 63 89 63
# 99 99 99
# 89 97 98

# 3
# 89 92 77
# 89 92 63
# 89 63 77


N = int(input())
score = [0] * N
num = [[]] * N
for _ in range(1):
    a, b, c = map(int,input().split())
    num[0].append(a)
    num[1].append(b)
    num[2].append(c)
# print(num) [[89, 92, 77], [89, 92, 77], [89, 92, 77]]

for i in range(3):
    for j in range(N):
        if num[i].count(num[i][j]) >= 2:
            score[j] += 0
        else:
            score[j] += num[i][j]

for k in score:
    print(k)









            
    
# n = int(input())
# score = [[], [], []]
# sum = []
 
# for i in range(n):
#     a, b, c = map(int, input().split())
#     score[0].append(a)
#     score[1].append(b)
#     score[2].append(c)
    
# for i in range(n):
#     get = 0
#     for j in range(3):
#         if score[j].count(score[j][i]) == 1:
#             get += score[j][i]
#     sum.append(get)
# for i in sum:
#     print(i)