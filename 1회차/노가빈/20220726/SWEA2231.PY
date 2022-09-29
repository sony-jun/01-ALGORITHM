num = int(input())
tempNum = 100
while True:
    tempNum += 1
    if tempNum+int(str(tempNum)[0])+int(str(tempNum)[1])+int(str(tempNum)[2]) == num:
        print(tempNum)
        break
