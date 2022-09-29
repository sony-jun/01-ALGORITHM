chess = [1,1,2,2,2,8]
find = list(map(int,input().split()))
result = []
for i in range(len(chess)):
    if find[i] != chess[i]:
        c = chess[i] - find[i]
    else : c = 0
    result.append(c)
result = map(str,result)
result = ' '.join(result)
print(result)
