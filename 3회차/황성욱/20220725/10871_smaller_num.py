n, x = map(int,input().split())
num_list = list(map(int,input().split()))
result = []
for num in num_list:
    if num < x:
        result.append(num)

for i in result:
    if i != result[-1]:
        print(i, end=' ')
    else:
        print(i)
    