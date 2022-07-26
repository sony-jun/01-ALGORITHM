# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

num1, num2 = map(int, input().split())
num1_list = []
num2_list = []

for i in range(1,num1+1):
    if num1%i == 0:
        num1_list.append(i)

for i in range(1,num2+1):
    if num2%i == 0:
        num2_list.append(i)        

list_ij = []
for i in num1_list:
    for j in num2_list:
        if i == j:
            list_ij.append(i) 
re1=list_ij.pop() #최대공약수 6
#최대공약수로 num1, num2 나눈 몫
q1 = num1 // re1
q2 = num2 // re1
re2 = re1 * q1 * q2

print(re1, re2, sep='\n')
