a, b = map(int, input().split())
a_com = set() # 최대 공약수를 구하기 위해서 차집합을 이용하려 집합으로 자료형 생성
b_com = set()


for i in range(1, a + 1): # 1 ~ a까지의 원소 중에 a 를 i로 나눈 나머지가 0이면 a의 약수라서 a_com 에 추가해줌
    if a % i == 0:
        a_com.add(i)

for j in range(1, b + 1): # 1 ~ b까지의 원소 중에 a 를 i로 나눈 나머지가 0이면 a의 약수라서 a_com 에 추가해줌
    if b % j == 0:
        b_com.add(j)

gcd = max(a_com & b_com) # 각 약수 리스트의 합 집합의 최댓값이 최대 공약수 
lcm = a * b // gcd # a * b 를 최대 공약수로 나눈값이 최소 공배수
print(gcd)
print(lcm)
