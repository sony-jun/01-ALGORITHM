# 숫자 받기
num1,num2 = input().split(' ')

#숫자 거꾸로
num1 = int(''.join(reversed(num1)))
num2 = int(''.join(reversed(num2)))

#거꾸로 한 숫자끼리 더한 후 다시 거꾸로
result = int(''.join(reversed(str(num1+num2))))

print(result)
