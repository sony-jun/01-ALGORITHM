# 1. 문제를 읽고 이해한다
#    a와b의 집합에서 a에서 b에 포함되는것 빼고
#    b에서 a가 포함되는것을 뺀 후 그 남은 원소의 개수를 더해라


# 2. 문제를 익숙한 용어로 재정의한다
# a = [1,2,4]

# b = [2,3,4,5,6]

# c = set(a) - set(b)
# print(c)
# d = set(b) - set(a)
# print(d)

# print(len(set(c)) + len(set(d)))

# 3. 어떻게 해결할지 계획을 세운다
 
# a의 집합과 b의 집합을 받아 줄 input()을 정의해주고
# a-b b-a를 새로 재정의해주고 그 c와d를 더해준다

# 4. 프로그램으로 구현한다
a , b = map(int,input().split())

c = set(map(int,input().split()))

d = set(map(int,input().split()))

print(len(set(c)-set(d)) + len(set(d)-set(c)))

# 5.어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다

# a,b = map(int,input().split())
# cnt = 0
# A = set(input().split())
# for i in input().split():
#     if i in A:
#         cnt+=1
# print(a+b-cnt*2)

# 반복문으로 푼 코드이다.
# a,b 집합의 수를 input
# set A는 input()
# for문에서 직접  B의 세트를 입력받고
# 만약 A와B가 겹치는게 있다면 
# 1씩 카운트하고 카운트한 수에 곱하기2를하고 A와 B의 더해 개수를 빼라