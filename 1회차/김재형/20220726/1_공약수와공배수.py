# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 24 18

import gc


A, B = map(int, input().split())

# 두 수를 나눠지지 않을 때까지 나누고 겹치는 부분이 최대공약수

# 두 수를 나눠지지 않을 때까지 나누고 겹치는 부분은 한번만 곱하고 나머지 다 곱하면 최대공배수
# 유클리드 호재법 큰수를 작은 수로 나누고 몫은 버리고 나머지를 다시 작았던 수와 나눠서 나머지가 0이 될 때까지

def gcf(A, B):
    while B > 0:
        A ,B = B, A % B
    return A

def lcm(A, B):
    return A * B // gcf(A, B)

print(gcf(A,B))
print(lcm(A,B))
    