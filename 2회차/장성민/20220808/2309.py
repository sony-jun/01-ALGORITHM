li = []
for _ in range(9):
    li.append(int(input()))

sum_li = sum(li)
one = 0
two = 0

for i in range(8):
    for j in range(i + 1, 9):
        if sum_li - (li[i] + li[j]) == 100:
            one = li[i]
            two = li[j]

li.remove(one)
li.remove(two)
li.sort()

for i in li:
    print(i)