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

# 답을 담을 곳
result = [0, 0, 0, 0, 0] 

game = []
for _ in range(N):
    game.append(list(map(int, input().split())))
#print(game) #[['100', '99', '98'], ['100', '97', '92'], ['63', '89', '63'], ['99', '99', '99'], ['89', '97', '98']]

a_ls = [] #[[100, 100, 63, 99, 89], [99, 97, 89, 99, 97], [98, 92, 63, 99, 98]]

# 열행으로 해서 같은 수있는지 확인하고 있으면 더하지 않는다.
for i in range(3):
    a = []
    for j in range(N):
        a.append(game[j][i])
        
    a_ls.append(a)

for i in range(3):
    a = a_ls[i]
    for j in range(N):
        b = a[j]
        if a.count(b) == 1:
            result[j] += b
for i in result:
    print(i)

            
    
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