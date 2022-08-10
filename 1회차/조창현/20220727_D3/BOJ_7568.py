# import sys

# sys.stdin = open("덩치.txt")

# T = int(input())
# people = []

# for i in range(T):
#     weight, height = map(int, input().split())
#     people.append((weight, height))
# #print(people)

# rank = [0] * T
# for i in people:
#     for j in people:
#         if i[0] > j[0] and i[1] > j[1]:
#             rank[j] += 1

# for i in rank:
#     print(i+1, end=" ")

#########################################################
#########################################################
#########################################################

import sys

sys.stdin = open("덩치.txt")

T = int(input())
people = []

for i in range(T):
    weight, height = list(map(int, input().split()))
    people.append((weight, height))
#print(people)

rank = [0] * T
for i in range(T):
    A = people[i]
    for j in range(T):
        B = people[j]
        if A[0] > B[0] and A[1] > B[1]:
            rank[j] += 1

for i in rank:
    print(i+1, end = " ")
