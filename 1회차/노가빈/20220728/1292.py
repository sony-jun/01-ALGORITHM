
# 숫자 받기
num1,num2 = map(int,input().split(' '))

if num1 <=1000 and num2 <=1000 and num1 >=1 and num2 >= 1:
    
    #numList 만들기
    numList = [0]
    i = 0
    while len(numList) <= num2:
        i += 1
        for j in range(i):
            numList.append(i)
            if len(numList) > num2:
                break

    #구간 값들 더하기
    result=0
    for i in range(num1,num2+1,1):
        result += numList[i]
    print(result)
else:
    print('다시 입력해주세요.')