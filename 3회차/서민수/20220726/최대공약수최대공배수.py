# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 예제 입력 1 
# 24 18
# 예제 출력 1 
# 6
# 72

# 24 18의 공통된 약수들 중 제일 큰것?
# 정수 인풋


# a,b의 입력값
a, b = map(int,input().split())
for i in range(1, a + 1):
    # 만약 a의 숫자와 i를 나눴을 때 나머지가 0 그리고 b 숫자와 i를 나눴을 때 
    if (a % i == 0) and (b % i == 0):
        # 그값은 c다!
        c = i


# 24 18 최소 공배수
c_lst = []
d_lst = []

for i in range(1, b+1):
    c_lst.append(i * a)
    # print(c_lst)
for i in range(1, a+1):
    # print(d_lst)
    d_lst.append(i*b)

# c_lst안에 i가 있다면
for i in c_lst:  
    # 만약 i가 d_lst에도 있다면
    if i in d_lst:
        #i = p다
        p = i
        break
print(c)
print(p)