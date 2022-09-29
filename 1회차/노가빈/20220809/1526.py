num = int(input())
i = 4
result1,result2 = 0,0
while True:
    if '4' in str(i) and '7' in str(i):
        if i <= num:
            result1 = i
        if i > num:
            result2 = i
            break
    i += 1

print(result1 if num-result1 < abs(num-result2) else abs(result2))