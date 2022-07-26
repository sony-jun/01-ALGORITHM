# 최대공약수와 최소공배수
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

#유클리드 호제
A, B = map(int, input().split())
a, b = A, B

while b != 0:
    a = a % b
    a, b = b, a

# gcd
print(a)

#lcm
print(A*B//a)