import sys
sys.stdin = open('2309.txt')
# 난쟁이 9명의 키를 리스트
numbers = [int(input()) for i in range(9)] 

# 9명의 키 - 7명의 키(100) 차이를 구한다.
total = sum(numbers)
gap = total - 100


for i in range(9-1): # (1 ~ 8)
    for j in range(i+1, 9): #(2 ~ 9) 중복을 없애기 위함
        if numbers[i] + numbers[j] == gap: 
            num1, num2 = numbers[i], numbers[j]
            break       

# 리스트에서 값을 제거
numbers.remove(num1)
numbers.remove(num2)
numbers.sort()

for k in range(len(numbers)):
    print(numbers[k])