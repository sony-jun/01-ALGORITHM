import sys
sys.stdin = open('B5533.txt')

# ppl = int(input())
# nums = [list(map(int,input().split())) for i in range(ppl)]
# p_list = [0] * ppl
# for i in range(3): 
#     points = 0
#     for j in range(ppl): 
#         if nums[j].count(nums[j][i]) < 2:
#             p_list[j] += nums[j][i]
# # print(p_list)

ppl = int(input())
round = [[], [], []]

for i in range(ppl):
    r1, r2, r3 = map(int, input().split())
    round[0].append(r1)
    round[1].append(r2)
    round[2].append(r3)

score = [0] * ppl

for i in range(3):
    for j in range(ppl):
        if round[i].count(round[i][j]) == 1:
            score[j] += round[i][j]
        
print(*score, sep='\n')

    
