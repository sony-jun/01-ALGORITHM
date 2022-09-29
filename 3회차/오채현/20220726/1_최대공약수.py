#최대공약수와 최소공배수

a, b = map(int, input().split())

#최대공약수: 두 수의 공통 약수 중 최댓값
for i in range(min(a, b), 0, -1): 
    #입력된 값 중 작은 수 부터 하나씩 줄여가며 입력 값들에 나누고 나머지가 0 일 경우 최대공약수가 되므로 출력하고 종료
    if a % i == 0 and b % i == 0:
        print(i)
        #최대공약수로 두 자연수를 나눈 두 몫을 다시 최대공약수와 함께 곱해주면 최소 공배수가 나옴!
        na = a // i
        nb = b // i
        minX = na * nb * i
        print(minX)

        break

#최소공배수: 두 수의 공통 배수 중 최솟값
for i in range(max(a, b),(a * b) + 1):
    #입력된 값 중 큰 수부터 입력된 두 값을 곱한 값까지 1씩 증가시키며 나가면서 그 값을 입력값들로 나눴을때 처음으로 나머지가 0 이 되는 값이 최소공배수이므로 출력하고 종료
    if i % a == 0 and i %b == 0:
        print(i)
        break


#math 함수사용

# import math

# a, b = map(int, input().split())
# print(math.gcd(a, b))
# print(math.lcm(a, b))

#유클리드 호제법

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))