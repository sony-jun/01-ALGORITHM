import sys

# f = open('bj2953.txt', 'r')
# print(f.readlines())

sys.stdin = open("bj2953.txt", 'r')

scorelist = {}
for i in range(1, 6) :
    score = list(map(int, input().split()))
    scorelist[sum(score)]= i 
    
max_ = max(list(scorelist.keys()))
print(scorelist[max_], max_)
