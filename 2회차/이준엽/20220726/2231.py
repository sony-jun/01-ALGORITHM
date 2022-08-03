n = int(input())
result = []

for i in range(n):
    strn = str(i)
    sum_ = 0
    for j in strn:
        sum_+=int(j)
    if i+sum_ == n :
        result.append(i)
if result == []:
    print(0)
else:
    print(min(result))