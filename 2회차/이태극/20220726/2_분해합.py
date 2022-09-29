target = int(input())
 
for i in range(target):
    temp = sum(map(int, str(i)))
    #숫자를 하나씩 잘라 합 구함
    result = i + temp
    #합과 0부터 반복문 돌려서 목표값과 같을때까지 반복
     
    if result == target:
        print(i)
        break
else:
    print(0)