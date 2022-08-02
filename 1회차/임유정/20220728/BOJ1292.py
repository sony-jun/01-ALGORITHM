# 쉽게 푸는 문제
A, B= map(int, input().split())

number = []
N=1
B=3
#for 조건문은 명확한 조건이 필요하다. 따라서 while을 이용
while len(number) < B:
    for i in range(N):
        number.append(N)
    N += 1
print(number)

