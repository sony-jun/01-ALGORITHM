
numList = []
for num in range(10):
    numList.append(input())
sum = 0
sum2 = 0
for i in range(len(numList)+1):
    numList[i] = int(numList[i])
    numList[i+1] = int(numList[i+1])
    sum += numList[i]
    sum2 += numList[i]
    if sum > 100-numList[i]:
        sum2 += numList[i+1]
        break
print(sum if 100-sum < sum2-100 else sum2)
