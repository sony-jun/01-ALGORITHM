## 최대공약수
a, b = input().split()
a_divisor = []
b_divisor = []
max_divisor = 0
## a의 약수를 구한다.
for i in range(1, int(a) + 1):
    if int(a) % i == 0:
        a_divisor.append(i)
#print(a_divisor)
## b의 약수를 구한다.
for i in range(1, int(b) + 1):
    if int(b) % i == 0:
        b_divisor.append(i)
#print(b_divisor)
## 두 약수들을 비교하여 같은 경우 최대공약수로 정해준다.
for i in a_divisor:
    for j in b_divisor:
        if i == j:
            max_divisor = i
print(max_divisor)

## 최소공배수 = 최대 공약수 * a를 최대공약수로 나눈 값 * b를 최대공약수로 나눈 값
a_multiple = int(a) / max_divisor
b_multiple = int(b) / max_divisor
min_multiple = a_multiple * b_multiple * max_divisor
print(int(min_multiple))
