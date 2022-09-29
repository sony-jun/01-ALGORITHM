import sys
sys.stdin = open("20220726/2609_최대공약수와최소공배수.txt")

num1, num2 = map(int, input().split())

for i in range(min(num1, num2), 0, -1): # 큰 수부터 1씩 감소하면서
    if num1 % i == 0 and num2 % i == 0: # 공약수 구하기
        divisor = i                     # 제일 먼저 나온 공약수가 최대공약수
        break                           # 반복문 탈출

multiple = num1 * num2 // divisor       # 최대공배수=(두 수의 곱)/최대공약수

print(divisor)  # 최대공약수 추력
print(multiple) # 최대공배수 출력