n = int(input())
temp = []
for i in range(666, 3000000):
    if '666' in str(i):
        temp.append(i)
        if len(temp) == 10000:
            break

print(temp[n-1])