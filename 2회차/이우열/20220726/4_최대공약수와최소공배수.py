a, b = map(int, input().split())
r = a if a < b else b                       # 최솟값까지 반복문 반복
arr = []

for i in range(1, r + 1):
    if a % i == 0 and b % i == 0:           # 공약수 구하기
        arr.append(i)                       # 공약수를 배열에 추가

gcd_ = arr[-1]                              # 최대공약수

lcm_ = (a // gcd_) * (b // gcd_) * gcd_     # 최소공배수

print(gcd_, lcm_, sep='\n')
