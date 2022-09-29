num = int(input())

for a in range(num) :
    if num == sum(map(int,str(a))) + a:
        result =a
        break
    else :
        result = 0

print(result)