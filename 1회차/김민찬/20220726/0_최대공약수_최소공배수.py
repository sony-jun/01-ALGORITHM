A, B = map(int, input().split()) # split()해주고 map()을 통해 A, B를 int로 형변환

for i in range(1, max(A, B)):
    if A % i == 0 and B % i == 0: # 공약수 중 가장 큰 수 = 최대공약수
        great = i # 1 ~ max(A, B)만큼 for문을 돌면서 A와 B로 모두 나누어지는 최대공약수

least = A * B // great #  A * B // 최대공약수 -> 최소공배수

print(great)
print(least)