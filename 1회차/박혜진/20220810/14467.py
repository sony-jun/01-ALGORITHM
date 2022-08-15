left = []
right = []

for _ in range(int(input())) :
   num, loc = map(int, input().split())

   if loc == 0 :
    left.append(num)

   else :
    right.append(num)

cnt = 0
# for l in left :
#     if l in right :
#         cnt += 1

print(cnt)