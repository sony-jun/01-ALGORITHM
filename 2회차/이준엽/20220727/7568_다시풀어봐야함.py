n = int(input())
people = []

for i in range(n):
    weight, height = map(int,input().split())
    people.append([weight,height])
# print(people,people[0])
for i in people:
    rank=1
    for j in people:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end=' ')

# n=int(input())
# peoples = []
# ranks = [0]*n
# for i in range(n):
#     weight,height = map(int,input().split())
#     peoples.append([weight,height])

# for a in range(n):
#     A = peoples[a]
#     for b in range(n):
#         B = peoples[b]

#         if A[0] > B[0] and A[1] > B[1]:
#             ranks[b]+=1

# for rank in ranks:
#     rank+=1
#     print(rank, end = ' ')
    