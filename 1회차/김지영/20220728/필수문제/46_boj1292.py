s,e = 3,7
lst = []

# n = 1
# while len(lst)<e:
#     for _ in range(n):
#         lst.append(n)
#     n += 1
# print(lst[s-1:e])

for i in range(1,e+1):
    for _ in range(e):
       lst.append(i)
print(sum(lst[s-1:e]))