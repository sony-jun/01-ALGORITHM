A, B = map(int, input().split())

sum_target = []

for i in range(1, 1001):
    for j in range(1, i+1):
        sum_target.append(i)
        
print(sum(sum_target[A-1:B]))
        