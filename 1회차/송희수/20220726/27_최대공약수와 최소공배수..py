import sys

sys.stdin = open("27_최대공약수와 최소공배수.txt")
x, y = map(int,input().split())
# 최대공약수는 각수를 나누고 나머지가 더이상 나누어지지 않는경우 그 몫의 값이다.
# 최소공배수는 각수를 나누고 나머지가 더이상 나누어 지지 않을때의 그나머지와 몫의 곱이다.
# tmp는 최대공약수의 약수
tmp = []

for i in range(1, min(x,y) + 1 ):
    # 각각의 x,y를 i로 나누어 떨어질때를 생각하였다.
    if x%i == 0 and y%i == 0:
        tmp.append(i)

print(max(tmp))
print(max(tmp)*(x//max(tmp))*(y// max(tmp)))
