# 키의 합이 100
# 브루트포스 알고리즘

small_people = [] 
sum_small = 0
for i in range(9):
    p = int(input())
    small_people.append(p)
small_people.sort()
for i in small_people:
    print(i)
    sum_small+=i
    if sum_small>100:
        break