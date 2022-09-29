at,bt = map(int,input().split(' '))
aList = list(map(int,input().split(' ')))
bList = list(map(int,input().split(' ')))

a_b_count = at
for i in aList:
    for j in bList:
        if j == i:
            a_b_count -= 1

b_a_count = bt
for i in bList:
    for j in aList:
        if j == i:
            b_a_count -= 1

print(a_b_count+b_a_count)