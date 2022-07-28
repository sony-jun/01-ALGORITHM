import sys
sys.stdin = open('나머지.txt','r')
numbers = []
#빈 리스트 생성
for _ in range(10): # 숫자 10개 입력받기
    n = int(input())
    numbers.append(n % 42) # 입력한 숫자를 42로 나눈 나머지를 numbers에 삽입
    

print(f'나머지 = {numbers}')
result = set(numbers)# 서로 다른 나머지가 몇 개 있는지 출력한다. => 중복 제거 

print(f'중복제거 후 나머지 = {result}')
print((len(result))) # result의 길이 출력