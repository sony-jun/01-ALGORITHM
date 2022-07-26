def check(num): # 각 자릿수 합 함수로 만들기
    result = [] 
    number = num
    for i in range(len(str(num))):
        result.append(number%10) # 1의자리 반환
        number = (number - (number%10))//10 #10을 나눠서 자릿수 줄이기
    return sum(result) #각자리수합
n = int(input())
result = [0] # 분해합 없으면 0
for i in range(n): 
    if i == check(n-i): #뺀 수와 빠진수의자리합이 같으면
        result.append(n-i) #생성자로 추가
print(result[-1]) #가장 마지막 추가된 생성자 출력