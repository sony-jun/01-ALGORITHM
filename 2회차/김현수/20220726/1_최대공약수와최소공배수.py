import sys

sys.stdin = open("1_최대공약수와최소공배수.txt",'r')

# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

#첫줄에 두개의 자연수 - 한 줄로 받아서 한 칸의 공백(split())으로 나누고 int형(map(int,aaa))으로 바꿔준다.
#최대 공약수는 동일하게 가지고 있는 약수의 합, 최소 공배수는 동일한 약수를 제외한 곱으로 출력가능
a, b = map(int,input().split())
a_1 = a # 최소공배수를 구하기 위한 초기값
b_1 = b #
a_ = [] 
b_ = [] 
c_ = 1 #최대공약수
 #최소공배수 = a * b /최대공약수
count_a = 2
while a != 1: #a의 약수 구하기
    if a % count_a == 0:
        a_.append(count_a)
        a = a / count_a
    else:
        count_a += 1

count_b = 2
while b != 1: #b의 약수 구하기
    if b % count_b == 0:
        b_.append(count_b)
        b = b / count_b
    else:
        count_b += 1

for i in range(len(a_)): #최대공약수 구하기
    for j in range(len(b_)):
        if a_[i] == b_[j]:
            c_ *= a_[i]
            b_[j] = 1 
            break

print(c_)
print(int(a_1*b_1/c_))